# izu.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json
import random
import urllib.parse


TITLE = '伊豆諸島の島'

FILE_LIST = 'data/izu_islands_list.json'

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

FILE_COLOR = 'data/web_colors_100.json'

FILE_HTML = 'izu_towns_shape.html'

TOKYO = '東京都'


# Miyakejima
lat_center = 34.08008
lon_center = 139.55908
ZOOM = 8


# CircleMarker
RADIUS = 20
COLOR = 'black',
FILL_COLOR = 'yellow',


# Popup
WIDTH = 100


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)


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


def style_function(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 2,
	"color":  'black',
	"fillColor": 'red'
    }
#


with open(FILE_LIST, 'r') as f2:
	dic2 = json.load(f2)
#


list_islands = dic2['islands']


with open(FILE_CATALOG, 'r') as f3:
    dic3 = json.load(f3)
#


url_raw_base = dic3['url_raw_base']

list_prefectures = dic3['prefectures']

towns = []


for item1 in list_islands:
	name_town = item1['name_town']
	towns.append(name_town)
#


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM, 
          tiles = "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
              attr = "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>",
              crs = 'EPSG3857')


for item2 in list_prefectures :
	pref_code = item2['code']
	pref_kanji = item2['kanji']
	list_cities = item2['cities']
	print(pref_kanji)
# Tokyo ?
	if pref_kanji != TOKYO:
		continue
	for item3  in list_cities: 
		name = item3['N03_004']
		filepath = item3['filepath']
		url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
# island town ?
		if name in towns:
			print(name)
			gjson = folium.GeoJson( url_geojson,
			style_function=style_function_random).add_to(map)
			folium.features.GeoJsonPopup( fields=['N03_004'], labels=False ).add_to(gjson)
#


# contries
for item in list_islands:
    name_island = item['name_island']
    lat = item['lat']
    lon = item['lon']
    print(name_island)
# Popup
    popup = folium.Popup(name_island, max_width= WIDTH)
# CircleMarker
    folium.CircleMarker(
    location = [lat, lon],
    radius= RADIUS,
    popup = popup,
    color= COLOR,
    fill= True,
    fill_color= FILL_COLOR,
).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILE_HTML)

