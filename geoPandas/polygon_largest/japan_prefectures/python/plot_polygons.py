# plot_prefs.py
# 2023-06-01 K.OHWAA

import folium
from folium.features import CustomIcon
import os
import json
import urllib.parse


FILE_LIST = 'data/japan_prefecture_coordinates_list.json'


FORMAT_TITLE = '<h3 align="center">{}</h3>'
 
FORMAT_POPUP_TITLE = '{pref} {city}'

FORMAT_FILENAME_HTML = '{name}.html'



ICON_WIDTH = 40

POPUP_WIDTH = 100

DIR_LARGEST = 'geojson_largest'

DIR_HTML = 'files'


# Tokyo Japan
lat_tokyo = 35.689722
lon_tokyo = 139.692222
ZOOM = 8


with open(FILE_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_prefectures = dic1['prefectures']


def find_pref(name_en):
	is_match = False
	item_name_pref = ''
	lat = 0
	lon = 0
	for item in list_prefectures:
		item_name_en = item['name_en']
		item_name_pref = item['name_pref']
		lat = item['lat']
		lon = item['lon']
		if item_name_en == name_en:
			is_match = True
			break
	return [is_match, 	item_name_pref, lat, lon]
#



def style_function(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 2,
	"color":  'red',
	"fillColor": 'yellow'
    }


if not os.path.isdir(DIR_HTML):
    os.mkdir(DIR_HTML)
#


files = os.listdir(DIR_LARGEST)


for item in files:
	filepath1 =  os.path.join(DIR_LARGEST, item)
	basename_without_ext = os.path.splitext(os.path.basename(filepath1))[0]
	print(basename_without_ext)
	filename = FORMAT_FILENAME_HTML.format(name=basename_without_ext)
	filepath2 =  os.path.join(DIR_HTML, filename)
	is_match, name_pref, lat, lon = find_pref(basename_without_ext)

# Map
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
# GeoJson
	gjson = folium.GeoJson(filepath1, style_function=style_function).add_to(map)
	folium.features.GeoJsonPopup( fields=['name'], labels=False ).add_to(gjson)
	title_html = FORMAT_TITLE.format(name_pref)
	map.get_root().html.add_child(folium.Element(title_html))

# save
	map.save(filepath2)
#
