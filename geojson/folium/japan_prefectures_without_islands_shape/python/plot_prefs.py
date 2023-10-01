# plot_prefs.py
# 2023-06-01 K.OHWAA

import folium
from folium.features import CustomIcon
import os
import json
import urllib.parse

FILE_LIST = 'data/japan_prefecture_coordinates_list.json'

FILE_CATALOG = 'data/japan_prefecture_without_islands_geojson_catalog.json'

FORMAT_TITLE = '<h3 align="center">{}</h3>'
 
FORMAT_POPUP_TITLE = '{pref} {city}'

FORMAT_FILENAME = '{name_en}.html'

ZOOM = 9

ICON_WIDTH = 40

POPUP_WIDTH = 100

DIR = 'files'


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#

with open(FILE_LIST , 'r') as f1:
    dic1 = json.load(f1)
#


list_prefectures1 = dic1['prefectures']


def find_pref(pref_code, name_ja):
	is_match = False
	marker = None
	for item in list_prefectures1:
		code =item['code']
		name_pref =item['name_pref']
		name_city = item['name_capital_city']
		url_flag = item['url_flag']
		flag_width = item['flag_width']
		flag_height = item['flag_height']
		lat = item['lat']
		lon = item['lon']
		if code == pref_code:
			is_match = True
			break
		if name_pref == name_ja:
			is_match = True
			break
	if is_match:
		popup_title = FORMAT_POPUP_TITLE.format(pref=name_pref, city=name_city)
		height = int( (ICON_WIDTH * flag_height) / flag_width )
		icon = CustomIcon(
        icon_image =  url_flag,
        icon_size = (ICON_WIDTH, height),
        icon_anchor = ( (ICON_WIDTH/2) , 0),
        popup_anchor = (0, 0)
    )
		popup = folium.Popup( popup_title, max_width= POPUP_WIDTH)
		marker = folium.Marker(location=[lat, lon], icon=icon, popup= popup)
	return marker
#


with open(FILE_CATALOG, 'r') as f2:
    dic2 = json.load(f2)
#

url_raw_base = dic2['url_raw_base']
list_prefectures2 = dic2['prefectures']
  

for item in list_prefectures2 :
	code = item['code']
	name_en = item['name_en']
	name_ja = item['name_ja']
	filename = item['filename']
	lat = item['lat']
	lon= item['lon']
	print(name_ja)
	url_geojson = urllib.parse.urljoin(url_raw_base, filename)
	save_name = FORMAT_FILENAME.format(name_en=name_en)
	save_path = os.path.join(DIR, save_name)
	marker = find_pref(code, name_ja)
# Map
	map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=ZOOM)
	folium.GeoJson(url_geojson ).add_to(map)
	marker.add_to(map)
	title_html = FORMAT_TITLE.format( name_ja)
	map.get_root().html.add_child(folium.Element(title_html))
	map.save(save_path)
#
