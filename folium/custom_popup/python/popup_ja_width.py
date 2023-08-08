# -*- coding: utf-8 -*-
# popup_ja.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup japanese width'

FILE_HTML = 'popup_ja_width.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'


# Yokohama Station
name = 'Yokohama Station'
name_ja = '横浜駅'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15

WIDTH = 100

# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

#Popup
popup = folium.Popup(name_ja, max_width=WIDTH)

# .Marker
folium.Marker(location=[lat, lon], popup=popup).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
