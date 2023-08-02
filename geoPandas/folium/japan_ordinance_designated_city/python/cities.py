# cities.py
# 2023-06-01 K.OHWAA

import folium
import os
import json
import urllib
import random


FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_CITY_LIST = 'data/japan_ordinance_designated_city_list.json'

FILE_COLOR = 'data/web_colors_100.json'

FORMAT_FILE_HTML = '{name}.html'


FORMAT_TITLE = '<h3 align="center">{pref} {city}</h3>'
 
DIR = 'cities'

ZOOM = 8


with open(FILE_CITY_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_designated_cities = dic1['cities']


with open(FILE_COLOR, 'r') as f2:
    dic2 = json.load(f2)
#

list_colors = dic2['colors']


def find_city(name, name_ja):
	is_match = False
	matched = None
	lat = 0
	lon = 0
	for item in 	list_designated_cities:
		item_name = item['name']
		item_name_ja = item['name_ja']
		if item_name == name:
			is_match = True
			matched = item
			break
		if item_name_ja == name_ja:
			is_match = True
			matched = item
			break
	if is_match:
		lat = matched['lat']
		lon = matched['lon']
	return[is_match, lat, lon]
#i


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


def read_json(filepath):
	with open(filepath) as f1:
		dic1 = json.load(f1) 
#
	features = dic1['features']
	feature = features[0]
	properties = feature['properties']
	prefecture = properties['prefecture']
	city = properties['city']
	return [prefecture, city]
#


with open(FILE_CATALOG, 'r') as f2:
    dic2 = json.load(f2)
#


url_raw_base = dic2['url_raw_base']
list_prefectures = dic2['prefectures']

files = os.listdir(DIR)


for item1 in files:
	name = os.path.splitext(os.path.basename(item1))[0]
	file_geojson =  os.path.join(DIR, item1)
	print(name)		
	pref_ja, city_ja = read_json(	file_geojson )
	print(pref_ja)
	print(city_ja)
	is_match, lat, lon = find_city(name, city_ja)
	title_html = FORMAT_TITLE.format(pref=pref_ja, city=city_ja)
	file_html = FORMAT_FILE_HTML.format(name=name)
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
	folium.GeoJson(	file_geojson, style_function=style_function_2).add_to(map)
	for item2 in list_prefectures:
		pref_code = item2['code']
		pref_kanji = item2['kanji']
		list_cities = item2['cities']
		print(pref_kanji)
		if pref_kanji != pref_ja:
			continue
		for item3  in list_cities:
			parent_city = item3['N03_003']
			city = item3['N03_004']
			filepath = item3['filepath']
			print(city)
			url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
			if parent_city == city_ja:
				gjson1 = folium.GeoJson(url_geojson, style_function=style_function_3).add_to(map)
				folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson1)
			else:
				gjson2 = folium.GeoJson(url_geojson, style_function=style_function_1).add_to(map)
				folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson2)
#
	map.get_root().html.add_child(folium.Element(title_html))
	map.save(file_html)
#

