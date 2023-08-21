# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'kanagawa_town_flag_list.json'

FILE_HTML = 'kanagawa_town_flag_list.html'


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


with open('files/template_row_colspan.txt', 'r') as f3:
    template_row_colspan = f3.read()
#


rows = ''

with open(FILE_JSON, 'r') as f4:
    dic = json.load(f4)
#

title_ja = dic['title_ja']

table_title_ja = dic['table_title_ja']

ref = dic['reference']

url_ref = dic['url_reference']

list_towns = dic['towns']


for item in list_towns :
    colspan = item['colspan']
    name_district = item['name_district']
    url_district = item['url_district']
    name_town = item['name_town']
    url_town = item['url_town']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    enactment = item['enactment']
    date = item['date']
    color = item['color']
    notes = item['notes']

    row_district = FORMAT_A_TAG.format(href=url_district, name=name_district)
    row_town = FORMAT_A_TAG.format(href=url_town, name=name_town)
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row = template_row.format(district=  row_district, town=row_town, flag=row_flag, enactment=enactment, date=date, color=color, notes=notes )
    row_colspan = template_row_colspan.format(colspan=colspan, district=  row_district, town=row_town, flag=row_flag, enactment=enactment, date=date, color=color, notes=notes )
    if colspan ==2:
        row = row_colspan
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, table_title=table_title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

