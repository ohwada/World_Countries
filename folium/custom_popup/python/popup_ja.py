# -*- coding: utf-8 -*-
# popup_ja.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup japanese'

FILE_HTML = 'popup_ja.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'


# Yokohama Station
name = 'Yokohama Station'
name_ja = '横浜駅'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15


# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=name_ja).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
