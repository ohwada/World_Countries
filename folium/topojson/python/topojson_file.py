# -*- coding: utf-8 -*-
# topojson_file.py
# 2023-06-01 K.OHWAA
# https://qiita.com/pork_steak/items/f551fa09794831100faa

import folium


TITLE = 'Japan  Prefectures'

FILE_TOPOJSON = 'data/japan.topojson'

FILE_HTML = 'topojson_file.html'

OBJECT_PATH = 'objects.japan'

NAME= 'japan'

FORMAT_TITLE = '''
             <h3 align="center">{}</h3>
             '''


# Tokyo Japan
name = 'Tokyo Japan'
lat = 35.689722
lon = 139.692222
ZOOM = 6


# Map
map = folium.Map(location=[lat, lon],
                  zoom_start=ZOOM ,
                  tiles='cartodbpositron')

# TopoJson
folium.TopoJson(
    data=open(    FILE_TOPOJSON, encoding='utf-8'),
    object_path = OBJECT_PATH,
    name = NAME
).add_to(map)


# add title
title_html = FORMAT_TITLE.format(TITLE)
map.get_root().html.add_child(folium.Element(title_html))


map.save(FILE_HTML)
