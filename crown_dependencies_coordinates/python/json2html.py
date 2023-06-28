# json2html.py
# 2023-06-01 K.OHWADA

import json

FORMAT_A_TAG = '<a href="{href}">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

FORMAT_ROWSPAN = 'rowspan="{rowspan}" '

ZOOM = 8

def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#

def make_rowspan(rowspan):
    if rowspan == 0:
        return ''
    ret = FORMAT_ROWSPAN.format(rowspan=rowspan)
    return ret
#

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

with open('template_row_island.txt', 'r') as f3:
    template_row_island = f3.read()

rows  = ''

with open('crown_dependencies_coordinates.json') as f4:
    dic = json.load(f4)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_teritories = dic['teritories']
    print(str_title)
    
    for item in list_teritories:
        id = item['id']
        group = item['group']
        rowspan = item['rowspan']
        teritory = item['teritory']
        url_teritory = item['url_teritory']
        island = item['island']
        url_island = item['url_island']
        capital = item['capital']
        url_capital = item['url_capital']
        url_flag = item['url_flag']
        flag_width = item['flag_width']
        flag_height = item['flag_height']
        lat = item['lat']
        lon = item['lon']
        print('id: ', id)
        print('group: ', group)
        print('rowspan: ', rowspan)
        row_teritory = FORMAT_A_TAG.format(href=url_teritory, name=teritory)
        row_island = FORMAT_A_TAG.format(href=url_island, name= island)
        row_capital = FORMAT_A_TAG.format(href=url_capital, name=capital)
        row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
        row_coordinates = make_coordinates(lat, lon)
        row_rowspan = make_rowspan(rowspan)

        if group == 0:
            row = template_row.format(teritory=row_teritory, island=row_island, capital=row_capital, flag=row_flag, coordinates=row_coordinates, rowspan= row_rowspan)
        else:
            row = template_row_island.format( island=row_island, capital=row_capital, flag=row_flag,  coordinates=row_coordinates )
        print(row)
        rows +=  row
#

html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('crown_dependencies_coordinates.html', 'w') as f5:
    f5.write(wdata)

