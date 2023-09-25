# -*- coding: utf-8 -*-
# json2html.py
# 2023-06-01 K.OHWADA

import os
import json
import urllib.parse


FILE_JSON = 'japan_prefecture_without_islands_geojson_catalog.json'

FILE_HTML  = 'japan_prefecture__without_islands_geojson_catalog.html'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

ZOOM = 11


def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#


with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#


with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#


rows = ''

with open(FILE_JSON, 'r') as f3:
    dic = json.load(f3)
#

str_title = dic['title']
title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
url_base = dic['url_base']
list_prefectures = dic['prefectures']
  
html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)


for item in list_prefectures :
    code = item['code']
    name_en = item['name_en']
    name_ja = item['name_ja']
    filename = item['filename']
    lat = item['lat']
    lon= item['lon']
    url_geojson = urllib.parse.urljoin(url_base, filename)
    row_filepath = FORMAT_A_TAG.format(href=url_geojson, name=filename)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format( code=code, name_en=name_en, name_ja=name_ja, filepath=row_filepath, coordinates=row_coordinates)
    print(row)
    rows +=  row
#


wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

