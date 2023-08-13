# tokyo.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = '東京都島嶼部の自治体の旗'

FILE_LIST = 'data/tokyo_islands_list.json'

FILE_HTML = 'tokyo_islands_flag.html'


# Miyakejima
lat_center = 34.08008
lon_center = 139.55908
ZOOM = 8

WIDTH = 100

FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)



with open(FILE_LIST , 'r') as f1:
    dic = json.load(f1)
#

list_municipalities = dic['municipalities']


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM)


# contries
for item in list_municipalities:
    name_municipality = item['name_municipality']
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
    popup = folium.Popup(name_municipality, max_width= WIDTH)
    folium.Marker(location=[lat, lon], icon=icon, popup= popup).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))


# save html file
map.save(FILE_HTML)

