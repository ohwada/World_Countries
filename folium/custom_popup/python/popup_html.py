# popup_html.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup html'

FILE_HTML = 'popup_html.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_HTML ='<b><font color="{color}">{name}</font></b>'

# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15


html =FORMAT_HTML.format(color='red', name=name)


# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=html).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
