# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'tokyo_23_wards_list.json'

FILE_HTML = 'tokyo_23_wards_lst.html'

FORMAT_A_TAG = '<a href="{href}">{name}</a>'

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
list_wards = dic['wards']


for item in list_wards :
    name_ward = item['name_ward']
    url_ward = item['url_ward']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    url_emblem = item['url_emblem']
    emblem_width = item['emblem_width']
    emblem_height = item['emblem_height']
    population = item['population']
    area = item['area']
    density = item['population_density']
    name_en = item['name_en']
    lat = item['lat']
    lon = item['lon']
    row_ward = FORMAT_A_TAG.format(href=url_ward, name=name_ward)
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row_emblem = FORMAT_IMG.format(src=url_emblem, width=emblem_width, height=emblem_height)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format(name_en=name_en, ward=row_ward, flag=row_flag, emblem=row_emblem, population=population, area =area, density=density, coordinates=row_coordinates)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

