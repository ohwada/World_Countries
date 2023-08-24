# ogasawara.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = '小笠原諸島の島'

FILE_LIST = 'data/ogasawara_islands_list.json'

URL_OGASAWARA = 'https://raw.githubusercontent.com/niiyz/JapanCityGeoJson/master/geojson/13/13421.json'

FILE_HTML = 'ogasawara_islands_shape.html'

# chichijima
lat_center = 27.077778
lon_center = 142.216667
ZOOM = 8


# CircleMarker
RADIUS = 50
COLOR = 'black',
FILL_COLOR = 'yellow',

# Popup
WIDTH = 100


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)


def style_function(feature):
	return {
	"fillOpacity": 0.1,
	"weight": 2,
	"color":  'black',
	"fillColor": 'red'
    }
#


with open(FILE_LIST , 'r') as f1:
    dic = json.load(f1)
#

list_islands = dic['islands']


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM, 
          tiles = "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
              attr = "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>",
              crs = 'EPSG3857')


# GeoJson
folium.GeoJson( URL_OGASAWARA,
style_function=style_function).add_to(map)


# contries
for item in list_islands:
    name_ja = item['name_ja']
    lat = item['lat']
    lon = item['lon']
    print(name_ja)
# Popup
    popup = folium.Popup(name_ja, max_width= WIDTH)
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

