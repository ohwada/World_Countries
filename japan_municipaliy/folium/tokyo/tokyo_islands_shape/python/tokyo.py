# -*- coding: utf-8 -*-
# tokyo.py
# 2023-06-01 K.OHWADA

import folium
import json
import requests
import random
import urllib.parse


TITLE = '東京都島嶼部の自治体'

FILE_LIST = 'data/tokyo_islands_list.json'

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'tokyo_islands_shape.html'

TOKYO = '東京都'

FORMAT_TITLE = '<h3 align="center">{}</h3>'


# Miyakejima
lat_center = 34.08008
lon_center = 139.55908
ZOOM = 8


with open(FILE_COLOR, 'r') as f1:
    dic = json.load(f1)
#

list_colors = dic['colors']


def style_function_1(feature):
	len_list = len( list_colors)
	rint = random.randint(0, (len_list -1) )
	item = list_colors[rint]
	color = item['hex']
	return {
	"fillOpacity": 0.5,
	"weight": 1,
	"color": "black",
	"fillColor": color
    }
#


def style_function_2(feature):
	color = 'red'
	return {
	"fillOpacity": 0.1,
	"weight": 3,
	"color":  color,
	"fillColor": color
    }
#


with open(FILE_LIST, 'r') as f2:
	dic2 = json.load(f2)
#


list_municipalities = dic2['municipalities']


with open(FILE_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#


url_raw_base = dic3['url_raw_base']

list_prefectures = dic3['prefectures']

municipalities = []


for item1 in list_municipalities:
	name_municipality = item1['name_municipality']
	municipalities.append(name_municipality)
#


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start= ZOOM, 
	tiles = "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
	attr = "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>",
	crs = 'EPSG3857')


for item2 in list_prefectures :
	pref_code = item2['code']
	pref_kanji = item2['kanji']
	list_cities = item2['cities']
	print(pref_kanji)
# Tokyo ?
	if pref_kanji != TOKYO:
		continue
	for item3  in list_cities: 
		name = item3['N03_004']
		filepath = item3['filepath']
		url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
# island municipality ?
		if name in municipalities:
			print(name)
			gjson = folium.GeoJson( url_geojson,
			style_function=style_function_1).add_to(map)
			folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)
#


# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))


map.save(FILE_HTML)

