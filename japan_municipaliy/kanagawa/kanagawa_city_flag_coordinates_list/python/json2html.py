# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'kanagawa_city_flag_coordinates_list.json'

FILE_HTML = 'kanagawa_city_flag_coordinates_list.html'


FORMAT_IMG = '<img src="{src}" width="{width}" height="{height}" />'

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

with open(FILE_JSON) as f3:
    dic = json.load(f3)
#

title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
list_cities = dic['cities']


for item in list_cities :
    group  = item['group']
    name_en  = item['name_en']
    name_city  = item['name_city']
    url_city = item['url_city']
    url_flag = item['url_flag']
    flag_width = item[f'flag_width']
    flag_height = item[f'flag_height']
    lat  = item['lat']
    lon  = item['lon']

    row_city  = FORMAT_A_TAG.format(href=url_city, name=name_city)
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format( group=group, name_en=name_en, city=row_city,flag=row_flag, coordinates=row_coordinates )
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

