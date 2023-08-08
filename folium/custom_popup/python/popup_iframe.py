# popup_html_iframe.py
# 2023-06-01 K.OHWAA

import folium
import branca

TITLE = 'Popup iframe'

FILE_HTML = 'popup_iframe.html'


FORMAT_TITLE = '<h3 align="center">{}</h3>'

FORMAT_A_TAG = '<a href="{href}">{name}</a>'


# Yokohama Station
name = 'Yokohama Station'
href= 'https://en.wikipedia.org/wiki/Yokohama_Station'
lat = 35.465833 
lon = 139.622778 
ZOOM = 15


html =FORMAT_A_TAG.format(href=href, name=name)

iframe = branca.element.IFrame(html=html, width=300, height=500)

#Popup
popup = folium.Popup(iframe, max_width=300)

# Map
map = folium.Map(location=[lat, lon], zoom_start=ZOOM)

# .Marker
folium.Marker(location=[lat, lon], popup=popup).add_to(map)

# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))

# save html file
map.save(FILE_HTML)
