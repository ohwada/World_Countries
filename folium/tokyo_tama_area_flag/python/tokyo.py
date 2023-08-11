# tokyo.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = '東京多摩地域の市町村の旗'


FILE_LIST = 'data/tokyo_tama_area_list.json'


FILE_HTML = 'tokyo_tama_area_flag.html'


# Tokyo Tama city
name = 'Tokyo Tama'
lat_center = 35.63694
lon_center = 139.44628
ZOOM = 12
WIDTH = 100


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
    name_ja = item['name_ja']
    name_en = item['name_en']
    url_city = item['url_city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    lat = item['lat']
    lon = item['lon']

# CustomIcon
    icon = CustomIcon(
        icon_image =  url_flag,
        icon_size = (flag_width, flag_height),
        icon_anchor = ( (flag_width/2) , 0),
        popup_anchor = (0, 0)
    )

# Marker
    popup = folium.Popup(name_ja, max_width= WIDTH)
    folium.Marker(location=[lat, lon], icon=icon, popup= popup).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILE_HTML)

