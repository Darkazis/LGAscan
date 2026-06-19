import streamlit as st
import pydeck as pdk
import sys
from pathlib import Path
from PIL import Image

# PAGE CONFIGURATION
try:
    img = Image.open("src/assets/logo.png")
    st.set_page_config(page_title="LGAScan Map", page_icon=img, layout="wide")
except FileNotFoundError:
    st.set_page_config(page_title="LGAScan Map", layout="wide")

st.title("🌏 Map View")

# DATA INGESTION
sys.path.append(str(Path(__file__).resolve().parents[2]))
# Only import the road geometries, leaving the evidence behind
from src.mockdata.sample_data import SAMPLE_ROADS

# SIDEBAR
st.sidebar.header("Map Settings")

# 1. Extract unique LGAs and create the first dropdown
all_lgas = set()
for road in SAMPLE_ROADS:
    for lga in road['lga'].split(','):
        all_lgas.add(lga.strip())
sorted_lgas = ["All Regions"] + sorted(list(all_lgas))

selected_lga = st.sidebar.selectbox("1. Filter by LGA", sorted_lgas)

# 2. Filter the road list based on the LGA selection
if selected_lga == "All Regions":
    filtered_roads = SAMPLE_ROADS
else:
    filtered_roads = [r for r in SAMPLE_ROADS if selected_lga in r['lga']]

# 3. Present the narrowed-down road list in the second dropdown
road_names = ["🗺️ View Entire NSW"] + [road['road_name'] for road in filtered_roads]
selected_name = st.sidebar.selectbox("2. Select a View", road_names)

# PYDECK CAMERA (ViewState) & LAYER LOGIC
# Default Camera
lat, lon = -32.5, 148.0
zoom_level = 5
layers = []

if selected_name != "🗺️ View Entire NSW":
    # Search within filtered_roads
    selected_road_data = next(r for r in filtered_roads if r['road_name'] == selected_name)
    
    first_coord = selected_road_data['segments'][0]['geometry']['coordinates'][0]
    lon, lat = first_coord[0], first_coord[1]
    zoom_level = 11.5
    
    geojson_feature = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": selected_road_data['geometry'],
                "properties": {"name": selected_road_data['road_name']}
            }
        ]
    }
    
    highlight_layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_feature,
        pickable=True,
        stroked=True,
        filled=False,
        get_line_color=[57, 255, 20], # Neon Green
        get_line_width=15,
        line_width_min_pixels=4, 
    )
    layers.append(highlight_layer)

view_state = pdk.ViewState(
    latitude=lat,
    longitude=lon,
    zoom=zoom_level,
    pitch=30, 
    bearing=0,
    transition_duration=1200, 
    transition_interruption=pdk.types.String("BREAK")
)

# RENDER NATIVE MAP
st.pydeck_chart(pdk.Deck(
    map_style="road",
    initial_view_state=view_state,
    layers=layers,
    tooltip={"html": "<b>Road:</b> {name}", "style": {"color": "white"}}
))