# geojson.py
# 2023-06-01 K.OHWAA

import folium
import requests
import json


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
antarctic_ice_edge = f"{url}/antarctic_ice_edge.json"
antarctic_ice_shelf_topo = f"{url}/antarctic_ice_shelf_topo.json"

# Antarctica
map = folium.Map(
    location=[-59.1759, -11.6016],
    tiles="cartodbpositron",
    zoom_start=2,
)

folium.GeoJson(antarctic_ice_edge, name="geojson").add_to(map)

folium.TopoJson(
    json.loads(requests.get(antarctic_ice_shelf_topo).text),
    "objects.antarctic_ice_shelf",
    name="topojson",
).add_to(map)

folium.LayerControl().add_to(map)


map.save('geojson.html')