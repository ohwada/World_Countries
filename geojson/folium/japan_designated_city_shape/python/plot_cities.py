# plot_cities.py
# 2023-06-01 K.OHWAA

import folium
import os
import json
import requests
import random
import urllib.parse


FILE_DESIGNATED_CATALOG = 'data/designated_cities_topojson_catalog.json'

FILE_PREF_CATALOG = 'data/japan_prefecture_geojson_catalog.json'

FILE_GEOJSON_CATALOG = 'data/japan_city_geojson_catalog.json'

FORMAT_FILE_HTML = '{dir}/{name}.html'

FORMAT_TITLE = '<h3 align="center">{pref} {city}</h3>'

ZOOM = 10

OBJECT_PATH = 'objects.city'

DIR = 'files'


def style_function_blue(feature):
	color = 'blue'
	return {
	"fillOpacity": 0.1,
	"weight": 5,
	"color": color,
	"fillColor": color
    }
#


def style_function_red(feature):
	color = 'red'
	return {
	"fillOpacity": 0.1,
	"weight": 3,
	"color": 'red',
	"fillColor": 'yellow'
    }
#


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#


with open(FILE_PREF_CATALOG, 'r') as f1:
    dic1 = json.load(f1)
#


url_raw_base1 = dic1['url_raw_base']

list_prefectures1 = dic1['prefectures']


def find_pref(pref_name):
	is_match = False
	url_geojson = ''
	for item1 in list_prefectures1:
		name_ja = item1['name_ja']
		filename = item1['filename']
		url_geojson = urllib.parse.urljoin(url_raw_base1, filename)
		if name_ja == pref_name:
			is_match = True
			break
	return[is_match, url_geojson]
#


with open(FILE_DESIGNATED_CATALOG, 'r') as f2:
    dic2 = json.load(f2)
#

url_designated_base = dic2['url_base']
list_designated_cities = dic2['cities']


with open(FILE_GEOJSON_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#

url_raw_base3 = dic3['url_raw_base']

list_prefectures3 = dic3['prefectures']




def style_function_black(feature):
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
	is_match, url_pref_geojson = find_pref(pref_name)
	print(city_name)
	title_html = FORMAT_TITLE.format(pref=pref_name, city=city_name)
	file_html = FORMAT_FILE_HTML.format(dir=DIR, name=name)
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
	gjson1 = folium.GeoJson( 
	url_pref_geojson, 
	style_function=style_function_blue).add_to(map)
	folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson1)
	folium.TopoJson( 
	json.loads(requests.get( url_topojson).text), 
    object_path = OBJECT_PATH, style_function=style_function_red).add_to(map)
	for item3 in list_prefectures3:
		pref_kanji = item3['kanji']
		list_cities = item3['cities']
		if pref_kanji != pref_name:
			continue
		print(pref_kanji)
		for item3 in list_cities:
			parent_city = item3['N03_003']
			city = item3['N03_004']
			filepath = item3['filepath']
			url_city_geojson = urllib.parse.urljoin(url_raw_base3, filepath)
			if parent_city == city_name:
				print(city)
				gjson3 = folium.GeoJson(url_city_geojson, style_function=style_function_black).add_to(map)
				folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson3)
	map.get_root().html.add_child(folium.Element(title_html))
	map.save(file_html)
#

