# itadori.py
# 2023-06-01 K.OHWAA

import folium
from folium.features import CustomIcon


# https://1upnoob.blogspot.com/2023/02/python-folium-custom-icon-marker.html

# Otsuna Kotohira Shrine
name = 'Otsuna Kotohira Shrine'
lat = 35.471028
lon = 139.624972
ZOOM = 15


# Icon
icon_file =   'itadori.png'
width = 100
height = 129
TITLE = 'Custom Icon (Itadori)'
FILENAME = 'itadori.html'


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)


# Map
map = folium.Map(location=[lat, lon], tiles="Stamen Terrain", zoom_start=ZOOM)

# CustomIcon
icon = CustomIcon(
    icon_image= icon_file, 
    icon_size=(width, height),
    icon_anchor=(width/2, height/2),
    popup_anchor=(0, -50)
)


# Marker
folium.Marker(location=[lat, lon], popup=name, icon=icon).add_to(map)

# add title
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILENAME)

