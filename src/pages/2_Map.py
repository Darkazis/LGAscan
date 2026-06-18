import streamlit as st
import leafmap.maplibregl as leafmap

import os
os.environ["MAPTILER_KEY"] = "znagUNG9r3YQ79JfhO9U"

from PIL import Image

# Pipeline Page Configuration Setup    
img = Image.open("src/assets/logo.png")

st.set_page_config(page_title="LGAScan", page_icon=img, layout="wide")
st.title("🌏 Map View")

# Map Rendering
MAPTILER_KEY = leafmap.get_api_key("MAPTILER_KEY")

m = leafmap.Map(
    center=[148, -33],
    zoom=5,
    style="streets")
source = {
    "type": "vector",
    "url": f"https://api.maptiler.com/tiles/countries/tiles.json?key={MAPTILER_KEY}",
}

m.add_source("statesData", source)
layer = {
    "id": "US_states",
    "source": "statesData",
    "source-layer": "administrative",
    "type": "fill",
    "filter": ["all", ["==", "level", 1], ["==", "level_0", "US"]],
    "paint": {
        "fill-color": [
            "match",
            ["get", "name"],
            "#D5CD85",
            [
                "New South Wales",
            ]
        ],
        "fill-opacity": 1,
        "fill-outline-color": "#000",
    },
}
first_symbol_layer_id = m.find_first_symbol_layer()["id"]
m.add_layer(layer, before_id=first_symbol_layer_id)
m.add_layer_control()

m.to_streamlit(height=550)