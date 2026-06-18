import streamlit as st
import leafmap.maplibregl as leafmap

from PIL import Image

# Pipeline Page Configuration Setup    
img = Image.open("src/assets/logo.png")

st.set_page_config(page_title="LGAScan", page_icon=img, layout="wide")
st.title("🌏 Map View")

# Side bar
st.sidebar.header("Map Settings")

# Map Rendering
m = leafmap.Map(
        center=[148, -33],
        min_zoom=5,
        style="streets",
        attribution_control=False,
    )

m.to_streamlit(height=550)