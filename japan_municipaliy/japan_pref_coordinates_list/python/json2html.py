# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'japan_prefecture_coordinates_list.json'

FILE_HTML = 'japan_prefecture_coordinates_list.html'


FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

WIDTH = 100

ZOOM = 12


def make_link(name, url):
    if not url:
        return name
    atag = FORMAT_A_TAG.format(href=url, name=name)
    return atag
#



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
list_prefectures = dic['prefectures']


for item in list_prefectures :
    code = item['code']
    name_en = item['name_en']
    name_pref = item['name_pref']
    url_pref = item['url_pref']
    name_capital = item['name_capital_city']
    url_capital = item['url_capital_city']
    url_icon = item['url_icon']
    icon_width = item['icon_width']
    icon_height = item['icon_height']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    lat = item['lat']
    lon = item['lon']

    row_pref = FORMAT_A_TAG.format(href=url_pref, name=name_pref)

    row_capital = FORMAT_A_TAG.format(href=url_capital, name=name_capital)

    row_icon = FORMAT_IMG.format(src=url_icon, width=icon_width, height=icon_height)

    height = int( (WIDTH * flag_height) / flag_width )

    row_flag = FORMAT_IMG.format(src=url_flag, width=WIDTH, height=height)

    row_coordinates = make_coordinates(lat, lon)

    row = template_row.format(code=code,  name_en=name_en, pref=row_pref, capital=row_capital, icon=row_icon, flag=row_flag,    coordinates=  row_coordinates )
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

