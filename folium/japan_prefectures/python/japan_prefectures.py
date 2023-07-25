# japan_prefectures.py
# 2023-06-01 K.OHWAA

import folium
import json
import random


TITLE = 'Japan Prefectures'

FILEPATH = 'japan_prefectures.html'

FORMAT_TITLE = '<h3 align="center">{}</h3>'
 
name = 'prefectures'
url_geojson = 'https://raw.githubusercontent.com/ohwada/World_Countries/master/folium/japan_prefectures/data/prefectures.geojson'

# Tokyo Japan
name = 'Tokyo Japan'
lat = 35.689722
lon = 139.692222
ZOOM = 4


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
	"weight": 2,
	"color": "black",
	"fillColor": color
    }
#


# Map
map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)

gjson = folium.GeoJson(url_geojson, name=name, style_function=style_function).add_to(map)

folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILEPATH )

