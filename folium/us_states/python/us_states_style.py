# us_states_style.py
# 2023-06-01 K.OHWAA

import folium
import requests
import json
import random

# https://github.com/python-visualization/folium/tree/main/examples/data


TITLE = 'States of USA in different Colors'

FILE_COLOR_JSON = 'data/web_colors_100.json'

FILE_HTML = 'us_states_style.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'
             
title_html = FORMAT_TITLE.format(TITLE)



url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
state_geo = f"{url}/us-states.json"


with open(FILE_COLOR_JSON, 'r') as f1:
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


# center of USA
map = folium.Map(location=[48, -102], tiles="cartodbpositron", zoom_start=3)

gjson = folium.GeoJson(state_geo, name="us-states", style_function=style_function).add_to(map)

folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson)

# add title
map.get_root().html.add_child(folium.Element(title_html))

map.save(FILE_HTML)

