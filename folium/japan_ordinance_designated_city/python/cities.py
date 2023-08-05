# cities.py
# 2023-06-01 K.OHWAA

import folium
import os
import json
import requests
import random
import urllib.parse


FILE_DESIGNATED_CATALOG = 'data/designated_cities_topojson_catalog.json'

FILE_GEOJSON_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_COLOR = 'data/web_colors_100.json'

FORMAT_FILE_HTML = '{dir}/{name}.html'

DIR = 'files'

FORMAT_TITLE = '<h3 align="center">{pref} {city}</h3>'

ZOOM = 10

OBJECT_PATH = 'objects.city'

with open(FILE_DESIGNATED_CATALOG, 'r') as f1:
    dic1 = json.load(f1)
#

url_designated_base = dic1['url_base']
list_designated_cities = dic1['cities']


with open(FILE_GEOJSON_CATALOG, 'r') as f2:
    dic2 = json.load(f2)
#

url_raw_base = dic2['url_raw_base']
list_prefectures = dic2['prefectures']


with open(FILE_COLOR, 'r') as f3:
    dic3 = json.load(f3)
#

list_colors = dic3['colors']


def style_function_1(feature):
	len_list = len( list_colors)
	rint = random.randint(0, (len_list -1) )
	item = list_colors[rint]
	color = item['hex']
	return {
	"fillOpacity": 0.5,
	"weight": 2,
	"color": "black",
	"fillColor": color
    }
#

def style_function_2(feature):
	color = 'red'
	return {
	"fillOpacity": 0.1,
	"weight": 5,
	"color": color,
	"fillColor": color
    }
#


def style_function_3(feature):
	return {
	"fillOpacity": 0.0,
	"weight": 1,
	"color": "black",
	"fillColor": "white"
    }
#


for item1 in list_designated_cities:
	pref_name = item1['N03_001']
	city_name = item1['N03_003']
	filepath = item1['filepath']
	name = item1['name']
	lat = item1['lat']
	lon = item1['lon']
	url_topojson = urllib.parse.urljoin(url_designated_base, filepath)
	print(city_name)
	title_html = FORMAT_TITLE.format(pref=pref_name, city=city_name)
	file_html = FORMAT_FILE_HTML.format(dir=DIR, name=name)
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
	folium.TopoJson( 
	json.loads(requests.get( url_topojson).text), 
    object_path = OBJECT_PATH, style_function=style_function_2).add_to(map)
	for item2 in list_prefectures:
		pref_kanji = item2['kanji']
		list_cities = item2['cities']
		if pref_kanji != pref_name:
			continue
		print(pref_kanji)
		for item3 in list_cities:
			parent_city = item3['N03_003']
			city = item3['N03_004']
			filepath = item3['filepath']
			url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
			if parent_city == city_name:
				print('inside: ', city)
				gjson1 = folium.GeoJson(url_geojson, style_function=style_function_3).add_to(map)
				folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson1)
			else:
				print('outside: ', city)
				gjson2 = folium.GeoJson(url_geojson, style_function=style_function_1).add_to(map)
				folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson2)
	map.get_root().html.add_child(folium.Element(title_html))
	map.save(file_html)
#

