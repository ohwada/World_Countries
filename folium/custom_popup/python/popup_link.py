# popup_link.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup link'

FILE_HTML = 'popup_link.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'


# Yokohama Station
name = 'Yokohama Station'
href= 'https://en.wikipedia.org/wiki/Yokohama_Station'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15


html =FORMAT_A_TAG.format(href=href, name=name)


# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=html).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
