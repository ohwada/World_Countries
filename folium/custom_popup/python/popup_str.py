# popup_str.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup string'

FILE_HTML = 'popup_str.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'


# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15


# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=name).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
