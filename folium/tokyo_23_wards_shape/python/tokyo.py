# -*- coding: utf-8 -*-
# tokyo.py
# 2023-06-01 K.OHWADA

import folium
import json
import requests
import random
import urllib.parse


TITLE = '東京23区'

URL_TOKYO_WARDS = 'https://geoshape.ex.nii.ac.jp/city/topojson/latest/13100.topojson'

OBJECT_PATH = 'objects.city'

FILE_LIST = 'data/tokyo_23_wards_list.json'

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'tokyo_23_wards_shape.html'

TOKYO = '東京都'

FORMAT_TITLE = '<h3 align="center">{}</h3>'


# Shinjyuku
lat = 35.6894
lon = 139.6917
ZOOM = 11


# Umi-no-Mori Park
# lat = 35.607333
# lon = 139.808167
# ZOOM = 13


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


list_wards = dic2['wards']


with open(FILE_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#


url_raw_base = dic3['url_raw_base']

list_prefectures = dic3['prefectures']

wards = []


for item1 in list_wards:
	name_ward = item1['name_ward']
	wards.append(name_ward)
#


map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start= ZOOM )


folium.TopoJson(
data = json.loads(requests.get( URL_TOKYO_WARDS ).text), 
object_path = OBJECT_PATH, 
style_function=style_function_2
).add_to(map)


for item2 in list_prefectures :
	pref_code = item2['code']
	pref_kanji = item2['kanji']
	list_cities = item2['cities']
	print(pref_kanji)
	if pref_kanji != TOKYO:
		continue
	for item3  in list_cities: 
		name = item3['N03_004']
		filepath = item3['filepath']
		url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
		if name in wards:
			print(name)
			gjson = folium.GeoJson( url_geojson,
			style_function=style_function_1).add_to(map)
			folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)
#


# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))


map.save(FILE_HTML)

