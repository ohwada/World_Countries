# kanagawa.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = '神奈川県の市町村旗'

FILE_LIST = 'data/kanagawa_city_flag_coordinates_list.json'

FILE_HTML = 'kanagawa_city_flag.html'


# Yokohama
name = 'Yokohama Japan'
lat_center = 35.45033
lon_center = 139.63422 
ZOOM = 10

FLAG_WIDTH = 40

POPUP_WIDTH = 100


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)



with open(FILE_LIST , 'r') as f1:
    dic = json.load(f1)
#

list_cities = dic['cities']


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM)


# contries
for item in list_cities:
    name_city = item['name_city']
    url_city = item['url_city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    lat = item['lat']
    lon = item['lon']

# CustomIcon
    height = int( (FLAG_WIDTH * flag_height) / flag_width )
    icon = CustomIcon(
        icon_image =  url_flag,
        icon_size = (FLAG_WIDTH, height),
        icon_anchor = ( (FLAG_WIDTH/2) , 0),
        popup_anchor = (0, 0)
    )

# Marker
    popup = folium.Popup(name_city, max_width= POPUP_WIDTH)
    folium.Marker(location=[lat, lon], icon=icon, popup= popup).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILE_HTML)

