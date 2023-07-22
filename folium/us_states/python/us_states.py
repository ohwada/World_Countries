# us_states.py
# 2023-06-01 K.OHWAA

import folium
import requests
import json

# https://github.com/python-visualization/folium/tree/main/examples/data

TITLE = 'States of USA'

FORMAT_TITLE = '<h3 align="center">{}</h3>'
             
title_html = FORMAT_TITLE.format(TITLE)


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)

state_geo = f"{url}/us-states.json"

# center of USA
map = folium.Map(location=[48, -102], tiles="cartodbpositron", zoom_start=3)

folium.GeoJson(state_geo, name="us-states").add_to(map)

# add title
map.get_root().html.add_child(folium.Element(title_html))

map.save('us_states.html')

