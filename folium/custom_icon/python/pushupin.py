# tokyo_japan_flag.py
# 2023-06-01 K.OHWAA

import folium
from folium.features import CustomIcon
from PIL import Image

# https://1upnoob.blogspot.com/2023/02/python-folium-custom-icon-marker.html

# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833
lon = 139.622778
ZOOM = 15


# Icon
url_icon = 'https://maps.google.com/mapfiles/ms/micons/red-pushpin.png'
width = 32
height = 32
TITLE = 'Costom Icon (Red Pushpin)'
FILENAME = 'pushupin.html'


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)


# center
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)


# CustomIcon
icon=CustomIcon(
	icon_image= url_icon,
	icon_size=(2*width, 2*height),
	icon_anchor=(width, height),
	popup_anchor=(0, -height)
 )


# Marker
folium.Marker(location=[lat, lon], popup=name, icon=icon).add_to(map)

# add title
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILENAME)

