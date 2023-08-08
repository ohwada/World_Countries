# popup_html_link.py
# 2023-06-01 K.OHWAA

import folium

TITLE = 'Popup image'

FILE_HTML = 'popup_img.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_IMG = '<img src="{src}" />'


# Yokohama Station
name = 'Yokohama Station'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15

# image
url_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Yokohama_sta._2022.jpg/320px-Yokohama_sta._2022.jpg'
width = 320
height = 192


html =FORMAT_IMG.format(src=url_img)


# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=html).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
