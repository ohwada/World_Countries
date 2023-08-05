# -*- coding: utf-8 -*-
# topojson_style.py
# 2023-06-01 K.OHWAA
# https://qiita.com/pork_steak/items/f551fa09794831100faa

import folium
import json
import random


TITLE = 'Japan Prefectures in different Colors'

FILE_TOPOJSON = 'data/japan.topojson'

FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'topojson_style.html'

OBJECT_PATH = 'objects.japan'

NAME= 'japan'

FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''


# Tokyo Japan
name = 'Tokyo Japan'
lat = 35.689722
lon = 139.692222
ZOOM = 6


with open(FILE_COLOR, 'r') as f1:
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
	"weight": 2,
	"color": "black",
	"fillColor": color
    }
#


# Map
map = folium.Map(location=[lat, lon],
                  zoom_start=ZOOM ,
                  tiles='cartodbpositron')

# TopoJson
gjson = folium.TopoJson(
    data=open(    FILE_TOPOJSON, encoding='utf-8'),
    object_path = OBJECT_PATH,
    name = NAME, 
    style_function=style_function
).add_to(map)

folium.features.GeoJsonPopup( fields=['nam_ja'], labels=False ).add_to(gjson)


# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))


map.save(FILE_HTML)
