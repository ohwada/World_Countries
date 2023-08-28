# -*- coding: utf-8 -*-
# kanagawa.py
# 2023-06-01 K.OHWADA

import folium
import json
import os
import requests
import random
import urllib.parse


TITLE = '神奈川県の市町村'

FILE_LIST = 'data/kanagawa_area_list.json'

FILE_CITY_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_DESIGNATED_CATALOG = 'data/designated_cities_topojson_catalog.json'

FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'kanagawa_area_shape.html'


URL_KANAGAWA = 'https://raw.githubusercontent.com/ohwada/World_Countries/main/geojson/japan_prefectures/geojson/kanagawa.geojson'


OBJECT_PATH = 'objects.city'

KANAGAWA = '神奈川県'

FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_FILE_HTML = '{name}.html'

DIR = 'files'


# Yokohama
name = 'Yokohama Japan'
lat = 35.45033
lon = 139.63422 
ZOOM = 10


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#


with open(FILE_COLOR, 'r') as f1:
    dic = json.load(f1)
#

list_colors = dic['colors']


def style_function_random(feature):
	len_list = len( list_colors)
	rint = random.randint(0, (len_list -1) )
	item = list_colors[rint]
	color = item['hex']
	return {
	"fillOpacity": 0.3,
	"weight": 1,
	"color": "black",
	"fillColor": color
    }
#


def style_function_black2(feature):
	return {
	"fillOpacity": 0,
	"weight": 2,
	"color":  'black',
	"fillColor": 'white'
    }
#


def style_function_black1(feature):
	return {
	"fillOpacity": 0,
	"weight": 1,
	"color":  'black',
	"fillColor": 'white'
    }
#


with open(FILE_LIST, 'r') as f2:
	dic2 = json.load(f2)
#


list_areas = dic2['areas']


with open(FILE_DESIGNATED_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#


url_base = dic3['url_base']

list_designated_cities = dic3['cities']

with open(FILE_CITY_CATALOG, 'r') as f4:
    dic4 = json.load(f4)
#


url_raw_base = dic4['url_raw_base']

list_prefectures = dic4['prefectures']


for item1 in list_areas:
	name_en = item1['name_en']
	name_area = item1['name_area']
	list_cities1 = item1['cities']

	title_html = FORMAT_TITLE.format(name_area)
	filename = FORMAT_FILE_HTML.format(name=name_en)
	file_html = os.path.join(DIR, filename)

# Map
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start= ZOOM )
# GeoJson
	folium.GeoJson( URL_KANAGAWA, style_function=style_function_black2).add_to(map)

	cities = []
	designated_cities = []

	for item2 in list_cities1:
		group = item2['group']
		name_city = item2['name_city']
		if group == 1:
			designated_cities.append(name_city)
		else:
			cities.append(name_city)

		for item3 in list_designated_cities: 
			name_ja = item3['N03_003']
			filepath = item3['filepath']
			url_topojson = urllib.parse.urljoin(url_base, filepath)
			if name_ja in designated_cities:
				print(name_ja)
# TopoJson
				gjson3 = folium.TopoJson(
				json.loads(requests.get( url_topojson).text), 
				object_path = OBJECT_PATH,
				style_function=style_function_random
				).add_to(map)
# GeoJsonPopup
				folium.features.GeoJsonPopup( fields=['N03_003'], labels=False ).add_to(gjson3)

		for item4 in list_prefectures :
			pref_code = item4['code']
			pref_kanji = item4['kanji']
			list_cities4 = item4['cities']
			print(pref_kanji)
# In Kanagawa ?
			if pref_kanji != KANAGAWA:
				continue
			for item5  in list_cities4: 
				parent = item5['N03_003']
				city = item5['N03_004']
				filepath = item5['filepath']
				url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
# in Kanagawa areas ?
				if city in cities:
					print(city)
# GeoJson
					gjson5 = folium.GeoJson( url_geojson,
					style_function=style_function_random).add_to(map)
# GeoJsonPopup
					folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson5)
				if parent in designated_cities:
					print(city)
# GeoJson
					gjson6 = folium.GeoJson( url_geojson,
					style_function=style_function_black1).add_to(map)
# GeoJsonPopup
					folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson6)

	map.get_root().html.add_child(folium.Element(title_html))
	map.save(file_html)
#


