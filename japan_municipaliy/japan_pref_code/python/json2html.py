# -*- coding: utf-8 -*-
# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'japan_prefecture_code_list.json'

FILE_HTML  = 'japan_prefecture_code_list.html'

FORMAT_REF = '<li><a href="{href}">{name}</a></li>'

FORMAT_REFS = '<ul>{refs}</ul>'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

WIDTH = 40

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
    str_title = dic['title']
    title_ja = dic['title_ja']
    ref1 = dic['reference1']
    url_ref1 = dic['url_reference1']
    ref2 = dic['reference2']
    url_ref2 = dic['url_reference2']
    list_prefectures = dic['prefectures']
  #
 
ref1 = FORMAT_REF.format(href=url_ref1, name=ref1)

ref2 = FORMAT_REF.format(href=url_ref2, name=ref2)

refs = ref1 + ref2

html_refs = FORMAT_REFS.format(refs=refs)

for item in list_prefectures :
    code = item['code']
    name = item['name']
    kanji = item['kanji']
    kana= item['kana']
    city = item['city']
    lat = item['lat']
    lon= item['lon']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    height = int( (WIDTH * flag_height) / flag_width )
    row_flag = FORMAT_IMG.format(src=url_flag, width=WIDTH, height=height)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format( code=code, name=name, kanji=kanji, kana=kana,  city=city, flag= row_flag, coordinates=row_coordinates)
    print(row)
    rows +=  row
#

wdata = template_html.format(body_title=title_ja, reference=html_refs, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

