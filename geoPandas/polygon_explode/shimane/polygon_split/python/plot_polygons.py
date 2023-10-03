# -*- coding: utf-8 -*-
# plot_polygons.py
# 2023-06-01 K.OHWADA

import folium
import json
import requests
import random
import urllib.parse
import csv
import os


TITLE = '分割されたポリゴン'


FILE_CSV = 'split_log.csv'


FILE_HTML = 'splited_polygons.html'


FORMAT_POPUP_TITLE = '{num} {place}'


FORMAT_TITLE = '<h3 align="center">{}</h3>'

DIR = 'geojson'


# CircleMarker
RADIUS = 20
COLOR = 'black',
FILL_COLOR = 'yellow',

# Popup
WIDTH = 100


# Matsue
lat = 35.4722
lon = 133.0503
ZOOM = 8



def style_function(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 2,
	"color":  'red',
	"fillColor": 'white'
    }
#


# .Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM, 
          tiles = "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
              attr = "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>",
              crs = 'EPSG3857')


with open(FILE_CSV, 'r') as f3:
    reader = csv.reader(f3)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 6:
            continue
        num = row[0].strip()
        lat = float( row[1].strip() )
        lon = float( row[2].strip() )
        place = row[3].strip()
        display = row[4].strip()
        filename = row[5].strip()

# GeoJson
        file_geojson =  os.path.join(DIR, filename)
        gjson = folium.GeoJson( file_geojson,
			style_function=style_function).add_to(map)
# GeoJsonPopup
 #       folium.features.GeoJsonPopup( fields=['place'], labels=False ).add_to(gjson)

# Popup
        popup_title =  FORMAT_POPUP_TITLE.format(num=num, place=place)
        popup = folium.Popup(popup_title , max_width= WIDTH)
# CircleMarker
        folium.CircleMarker(
    location = [lat, lon],
    radius= RADIUS,
    popup = popup,
    color= COLOR,
    fill= True,
    fill_color= FILL_COLOR,
).add_to(map)
#


title_html = FORMAT_TITLE.format( TITLE )
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILE_HTML)
