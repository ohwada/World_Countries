# toyama.py
# 2023-06-01 K.OHWAA

import folium
import json


TITLE = '富山県 中新川郡 下新川郡'

desc = '赤: 中新川郡  青:下新川郡'

FILE_TOYAMA = 'data/N03-21_16_210101.json'

FILE_NAKANIIKAWA = 'data/nakaniikawa.geojson'

FILE_SHIMONIIKAWA = 'data/shimoniikawa.geojson'

FILE_HTML = 'toyama.html'

FORMAT_TITLE = '<h3 align="center">{title}</h3><div align="center">{desc}</div>'
 


# Toyama
name = 'Toyama'
lat = 36.69531
lon = 137.21131
ZOOM = 9


def style_function_1(feature):
	color = 'red'
	return {
	"fillOpacity": 0.1,
	"weight": 4,
	"color": color,
	"fillColor": color
    }
#

def style_function_2(feature):
	color = 'blue'
	return {
	"fillOpacity": 0.1,
	"weight": 4,
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


# Map
map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)

# GeoJson
folium.GeoJson(FILE_NAKANIIKAWA, style_function=style_function_1).add_to(map)

folium.GeoJson(FILE_SHIMONIIKAWA, style_function=style_function_2).add_to(map)

# GeoJson
gjson = folium.GeoJson(FILE_TOYAMA, style_function=style_function_3).add_to(map)

# GeoJsonPopup
folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)


# add title
title_html = FORMAT_TITLE.format(title=TITLE, desc=desc)
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILE_HTML)

