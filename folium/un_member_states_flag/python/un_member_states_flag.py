# un_member_states_flag.py
# 2023-06-01 K.OHWADA

import folium
from folium.features import CustomIcon
import json


TITLE = 'National Flag at the Capital of member States of United Nations'

FILENAME = 'un_member_states_flag.html'


# center
# on the equator at the same longitude as India
lat_center = 0
lon_center = 77.209006
ZOOM = 2


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)



with open('un_members_capital.json') as f4:
    dic = json.load(f4)
    list_countries = dic['countries']
#


# Map
map = folium.Map(location=[lat_center, lon_center], zoom_start=ZOOM)


# contries
for item in list_countries:
    country = item['country']
    url_country = item['url_country']
    url_flag_icon = item['url_flag_icon']
    icon_width = item['icon_width']
    icon_height = item['icon_height']
    lat = item['lat']
    lon = item['lon']

# CustomIcon
    icon = CustomIcon(
        icon_image =  url_flag_icon,
        icon_size = (icon_width, icon_height),
        icon_anchor = ( (icon_width/2) , 0),
        popup_anchor = (0, 0)
    )

# Marker
    folium.Marker(location=[lat, lon], icon=icon, popup= country).add_to(map)
#


# add title
map.get_root().html.add_child(folium.Element(title_html))



# save html file
map.save(FILENAME)

