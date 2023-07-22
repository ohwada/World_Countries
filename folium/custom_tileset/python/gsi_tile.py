# -*- coding: utf-8 -*-
# gsi_tile.py
# 2023-06-01 K.OHWAA

import folium

# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833
lon = 139.622778
ZOOM = 15

TITLE = '地理院タイル'

FILENAME = 'gsi_tile.html'


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)

map = folium.Map(location = [lat, lon],
              zoom_start = ZOOM,
              tiles = "https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png",
              attr = "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>",
              crs = 'EPSG3857')

# add title
map.get_root().html.add_child(folium.Element(title_html))

# marker(yokohama Station)
folium.Marker(location=[lat, lon], popup=name).add_to(map)

map.save(FILENAME)
