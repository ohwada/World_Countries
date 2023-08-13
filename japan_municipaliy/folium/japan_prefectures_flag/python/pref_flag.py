# pref_flag.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = '都道府県の県旗'

FILE_LIST = 'data/japan_prefecture_code_list.json'

FILE_HTML = 'japan_prefectures_flag.html'


# Tokyo Japan
name = 'Tokyo Japan'
lat_center = 35.689722
lon_center = 139.692222
ZOOM = 6

WIDTH = 40


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

FORMAT_POPUP_TITLE = '{pref} {city}'

title_html = FORMAT_TITLE.format(TITLE)



with open(FILE_LIST , 'r') as f1:
    dic = json.load(f1)
#

list_prefectures = dic['prefectures']


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM)


# contries
for item in list_prefectures:
    pref_name = item['kanji']
    city_name = item['city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    lat = item['lat']
    lon = item['lon']
    popup_title = FORMAT_POPUP_TITLE.format(pref=pref_name, city=city_name)
    height = int( (WIDTH * flag_height) / flag_width )
# CustomIcon
    icon = CustomIcon(
        icon_image =  url_flag,
        icon_size = (WIDTH, height),
        icon_anchor = ( (WIDTH/2) , 0),
        popup_anchor = (0, 0)
    )

# Marker
    popup = folium.Popup( popup_title, max_width= WIDTH)
    folium.Marker(location=[lat, lon], icon=icon, popup= popup).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILE_HTML)

