# -*- coding: utf-8 -*-
# plot_brfore.py
# 2023-06-01 K.OHWADA

import folium
import json
import requests
import random
import urllib.parse
import csv
import os

TITLE = '北海道 分割前'

FILE_GEOJSON = 'data/hokkaido.geojson'

FILE_HTML = 'hokkaido_brfore.html'

FORMAT_TITLE = '<h3 align="center">{}</h3>'


DIR = 'dst_geojson'


# CircleMarker
RADIUS = 50
COLOR = 'black',
FILL_COLOR = 'yellow',

# Popup
WIDTH = 100


# Sapporo
lat = 43.38349012194063
lon = 142.57126343619075
ZOOM = 6







def style_function(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 2,
	"color":  'red',
	"fillColor": 'yellow'
    }
#

# Map
map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
# GeoJson
gjson = folium.GeoJson( FILE_GEOJSON,
	style_function=style_function).add_to(map)

folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson)

title_html = FORMAT_TITLE.format( TITLE )
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILE_HTML)
