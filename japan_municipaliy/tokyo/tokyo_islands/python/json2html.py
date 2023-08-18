# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'tokyo_islands_list.json'

FILE_HTML = 'tokyo_islands_lst.html'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'


ZOOM = 12


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

title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
list_municipalities = dic['municipalities']


for item in list_municipalities :
    number = item['number']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    name_municipality = item['name_municipality']
    url_municipality = item['url_municipality']
    name_location = item['name_location']
    url_location = item['url_location']
    name_en = item['name_en']
    lat = item['lat']
    lon = item['lon']
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row_municipality = FORMAT_A_TAG.format(href=url_municipality, name=name_municipality)
    row_location = FORMAT_A_TAG.format(href=url_location, name=name_location)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format(number=number, flag=row_flag, municipality=row_municipality, name_en=name_en, location=row_location,coordinates=row_coordinates)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

