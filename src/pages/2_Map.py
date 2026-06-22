import sys
from pathlib import Path
import requests
import folium
import streamlit as st
from PIL import Image
from streamlit_folium import st_folium

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
try:
    img = Image.open("src/assets/logo.png")
    st.set_page_config(page_title="LGAScan Map", page_icon=img, layout="wide")
except FileNotFoundError:
    st.set_page_config(page_title="LGAScan Map", layout="wide")

st.title("🌏 Interactive Map View")

# ==========================================
# 2. DATA INGESTION
# ==========================================
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.mockdata.sample_data import SAMPLE_ROADS

# ==========================================
# 3. ROUTING ENGINE (The Brains)
# ==========================================
def get_road_curve(coord_a, coord_b):
    """Pings the OSRM routing server to get the exact road curvature."""
    lon1, lat1 = coord_a[1], coord_a[0]
    lon2, lat2 = coord_b[1], coord_b[0]
    
    url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    try:
        response = requests.get(url).json()
        if "routes" in response and len(response["routes"]) > 0:
            return response["routes"][0]["geometry"]
    except Exception:
        st.error("Routing engine offline or unreachable.")
    return None

# ==========================================
# 4. SIDEBAR LOGIC (The Camera Controller)
# ==========================================
st.sidebar.header("Map Settings")

# Extract unique LGAs
all_lgas = set()
for road in SAMPLE_ROADS:
    for lga in road['lga'].split(','):
        all_lgas.add(lga.strip())
sorted_lgas = ["All Regions"] + sorted(list(all_lgas))

selected_lga = st.sidebar.selectbox("Filter by LGA", sorted_lgas)

# Filter the road list based on the LGA selection
if selected_lga == "All Regions":
    filtered_roads = SAMPLE_ROADS
else:
    filtered_roads = [r for r in SAMPLE_ROADS if selected_lga in r['lga']]

road_names = ["🗺️ View Entire NSW"] + [road['road_name'] for road in filtered_roads]
selected_name = st.sidebar.selectbox("Select a View", road_names)

# ==========================================
# 5. MAP STATE & RENDER LOGIC
# ==========================================
# Default Camera (Zoomed out over NSW)
lat, lon = -32.5, 148.0
zoom_level = 5

# If a user selects a road in the sidebar, instantly zoom the camera to it
if selected_name != "🗺️ View Entire NSW":
    selected_road_data = next(r for r in filtered_roads if r['road_name'] == selected_name)
    # Grab the first coordinate of the road to center the camera
    first_coord = selected_road_data['segments'][0]['geometry']['coordinates'][0]
    lon, lat = first_coord[0], first_coord[1]
    zoom_level = 14  # Zoom in close so it's easy to click

st.markdown(f"**Current Area:** {selected_name}")
st.info("🖱️ **Interaction:** Click two points on the map below to snap to the physical road.")

# Initialize our click memory
if "map_clicks" not in st.session_state:
    st.session_state.map_clicks = []

# Build the Base Map
m = folium.Map(location=[lat, lon], zoom_start=zoom_level)

# Draw pins for any existing clicks
for i, coord in enumerate(st.session_state.map_clicks):
    folium.Marker(coord, tooltip=f"Point {i+1}", icon=folium.Icon(color="blue")).add_to(m)

# The Magic: If we have 2 points, draw the curved route
if len(st.session_state.map_clicks) == 2:
    point_a = st.session_state.map_clicks[0]
    point_b = st.session_state.map_clicks[1]
    
    with st.spinner("Calculating road curvature..."):
        curve_geojson = get_road_curve(point_a, point_b)
        
    if curve_geojson:
        folium.GeoJson(
            curve_geojson, 
            name="Selected Road Segment",
            style_function=lambda x: {'color': '#0078D7', 'weight': 6, 'opacity': 0.85}
        ).add_to(m)

# Render the map to Streamlit, passing back browser events
map_data = st_folium(m, use_container_width=True, height=650)

# Process brand new clicks from the browser
if map_data and map_data.get("last_clicked"):
    click_lat = map_data["last_clicked"]["lat"]
    click_lon = map_data["last_clicked"]["lng"]
    new_coord = (click_lat, click_lon)
    
    # If they click a 3rd time, clear the board and start a new route
    if len(st.session_state.map_clicks) >= 2:
        st.session_state.map_clicks = [new_coord]
    elif new_coord not in st.session_state.map_clicks:
        st.session_state.map_clicks.append(new_coord)
        
    st.rerun()  # Force Streamlit to refresh and draw the new point