# tokyo_japan_flag.py
# 2023-06-01 K.OHWAA

import folium
from folium.features import CustomIcon


# Tokyo Japan
name = 'Tokyo Japan'
lat = 35.689722
lon = 139.692222
ZOOM = 4

# Icon

url_icon = 'https://raw.githubusercontent.com/ohwada/World_Countries/master/folium/tokyo_japan_flag/images/40px-Flag_of_Japan.png'

# url_icon = 'https://raw.githubusercontent.com/ohwada/World_Countries/master/leaflet/tokyo_japan_flag/images/40px-Flag_of_Japan.png'

width = 40
height = 26

TITLE = 'Japan Flag at Tokyo Japan'
FILENAME = 'tokyo_japan_flag.html'


FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''

title_html = FORMAT_TITLE.format(TITLE)


# center( Tokyo Japan)
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)


# CustomIcon
icon = CustomIcon(
   icon_image =  url_icon
   ,icon_size = (width, height)
   ,icon_anchor = ( (width/2) , 0)
   ,popup_anchor = (0, 0)
)

# marker( Tokyo Japan)
folium.Marker(location=[lat, lon], popup=name, icon=icon).add_to(map)

# add title
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILENAME)

