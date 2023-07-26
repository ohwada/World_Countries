# -*- coding: utf-8 -*-
# kanagawa.py
# 2023-06-01 K.OHWADA

import folium
import json
import random

TITLE = '神奈川県の市町村'

FILEPATH = 'kanagawa.html'

# kanagawa
CODE_KANAGAWA = '14'

FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_URL = 'https://raw.githubusercontent.com/niiyz/JapanCityGeoJson/master/{path}'

  
# Yokohama Japan
name= 'Yokohama Japan'
lat = 35.45033
lon = 139.63422
ZOOM = 10


with open('web_colors_100.json') as f1:
    dic = json.load(f1)
#

list_colors = dic['colors']


def style_function(feature):
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

      
with open('japan_city_geocode_catalog.json') as f4:
    dic = json.load(f4)
#


list_prefectures = dic['prefectures']

map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start= ZOOM )


for item1 in list_prefectures :
	pref_code = item1['code']
	pref_kanji = item1['kanji']
	list_cities = item1['cities']
	print(pref_kanji)
	if pref_code != CODE_KANAGAWA:
		continue

	for item2 in list_cities: 
		city_code = item2['code']
		city_kanji = item2['kanji']
		filepath = item2['filepath']
		print(city_kanji)
		url_geojson = FORMAT_URL.format(path=filepath)
		gjson = folium.GeoJson( url_geojson, name=city_kanji, style_function=style_function).add_to(map)
		folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)
#


# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILEPATH)

