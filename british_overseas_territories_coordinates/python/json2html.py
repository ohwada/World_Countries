# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

TEMPLATE_LATLON = '({lat:.1f}, {lon:.1f})'

ZOOM = 8

def make_coordinates(lat, lon):
    gmap = TEMPLATE_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =TEMPLATE_LATLON.format( lat=lat, lon=lon )
    atag =TEMPLATE_A_TAG.format(href=gmap, name=latlon)
    return atag
#

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

countries =[]

rows=""

with open('british_overseas_territories_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_territories = dic['territories']
    
    for item in list_territories:
        country = item['territory']
        url_country = item['url_territory']
        capital = item['capital']
        url_capital = item['url_capital']
        url_flag  = item['url_flag']
        flag_width = item['flag_width']
        flag_height = item['flag_height']
        lat = item['lat']
        lon = item['lon']
        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        row_capital = TEMPLATE_A_TAG.format(href=url_capital, name=capital)
        row_flag = TEMPLATE_IMG.format(src=url_flag, width=flag_width, height=   flag_height)
        row_coordinates = make_coordinates(lat, lon)
        row = template_row.format(country=row_country, capital=row_capital, flag=row_flag, coordinates=row_coordinates)
        print(row)
        rows +=  row
#
html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('british_overseas_territories_coordinates.html', 'w') as f4:
    f4.write(wdata)

