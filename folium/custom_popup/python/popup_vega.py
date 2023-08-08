# popup_vega.py
# 2023-06-01 K.OHWAA
# https://python-visualization.github.io/folium/quickstart.html#Vincent/Vega-and-Altair/VegaLite-Markers

import folium
import json
import requests

TITLE = 'Popup vega'

FILE_HTML = 'popup_vega.html'

FORMAT_TITLE = '<h3 align="center">{}</h3>'

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)

url_vis1 = f"{url}/vis1.json"

vis1 = json.loads(requests.get(url_vis1).text)

# Seattle
lat = 46.3014
lon = -123.7390
zoom = 7


# Map
map = folium.Map( location=[lat, lon], zoom_start=zoom )

# Vega
vega1 = folium.Vega(vis1, width=450, height=250)

# .Popup
popup = folium.Popup(max_width=450).add_child(vega1)

# .Marker
folium.Marker(
    location=[lat, lon],
    popup=popup ).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
