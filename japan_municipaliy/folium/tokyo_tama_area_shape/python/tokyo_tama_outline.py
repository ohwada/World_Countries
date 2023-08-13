# -*- coding: utf-8 -*-
# tokyo.py
# 2023-06-01 K.OHWADA

import folium
import json
import requests
import random
import urllib.parse


TITLE = '東京多摩地域の市町村'

desc = '赤: 東京都の外形 緑: 多摩西部の外形 青: 多摩東部の外形 黄色: 東京23区'

FILE_LIST = 'data/tokyo_tama_area_list.json'

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

URL_TOKYO = 'https://raw.githubusercontent.com/ohwada/World_Countries/main/geojson/japan_prefectures/geojson/tokyo.geojson'

URL_TOKYO_TAMA_EAST = 'https://geoshape.ex.nii.ac.jp/jma/resource/AreaForecastLocalE/20190125/351.geojson'

URL_TOKYO_TAMA_WEST = 'https://geoshape.ex.nii.ac.jp/jma/resource/AreaForecastLocalE/20190125/352.geojson'

URL_TOKYO_23_WARDS = 'https://geoshape.ex.nii.ac.jp/jma/resource/AreaForecastLocalE/20190125/350.geojson'


FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'tokyo_tama_area_shape_outline.html'

TOKYO = '東京都'


FORMAT_TITLE = '<h3 align="center">{body_title}</h3><div align="center">{desc}</div>'



# Tokyo Tama city
name = 'Tokyo Tama'
lat = 35.63694
lon = 139.44628
ZOOM = 11


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
	"fillOpacity": 0.5,
	"weight": 1,
	"color": "black",
	"fillColor": color
    }
#


def style_function_red(feature):
	return {
	"fillOpacity": 0,
	"weight": 5,
	"color":  'red',
	"fillColor": 'white'
    }
#


def style_function_blue(feature):
	color = 'blue'
	return {
	"fillOpacity": 0,
	"weight": 4,
	"color":  'blue',
	"fillColor": 'white'
    }
#


def style_function_green(feature):
	return {
	"fillOpacity": 0,
	"weight": 3,
	"color":  'green',
	"fillColor": 'white'
    }
#


def style_function_yellow(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 3,
	"color":  'black',
	"fillColor": 'yellow'
    }
#


with open(FILE_LIST, 'r') as f2:
	dic2 = json.load(f2)
#


list_cities = dic2['cities']


with open(FILE_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#


url_raw_base = dic3['url_raw_base']

list_prefectures = dic3['prefectures']


cities = []

for item1 in list_cities:
	name_ja = item1['name_ja']
	cities.append(name_ja)
#


# Map
map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start= ZOOM )


# GeoJson
folium.GeoJson( URL_TOKYO,
style_function=style_function_red).add_to(map)


gjson1 = folium.GeoJson( URL_TOKYO_23_WARDS,
style_function=style_function_yellow).add_to(map)
folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson1)

folium.GeoJson( URL_TOKYO_TAMA_WEST,
style_function=style_function_green).add_to(map)

folium.GeoJson( URL_TOKYO_TAMA_EAST,
style_function=style_function_blue).add_to(map)



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
		if name in cities:
			print(name)
			gjson = folium.GeoJson( url_geojson,
			style_function=style_function_random).add_to(map)
			folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)
#


# add title
title_html = FORMAT_TITLE.format(body_title=TITLE, desc =desc)
map.get_root().html.add_child(folium.Element(title_html))


map.save(FILE_HTML)

