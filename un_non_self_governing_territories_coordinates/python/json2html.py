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

def make_a_tag(name, href):
    if not href:
        return name
    ret = TEMPLATE_A_TAG.format(href=href, name=name)
    return ret
#


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

territories =[]

rows=""

with open('un_non_self_governing_territories_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_territories = dic['territories']
    print(str_title)
    
    for item in list_territories:
        territory = item['territory']
        url_territory = item['url_territory']
        url_territory_flag = item['url_territory_flag']
        territory_width = item['territory_width']
        territory_height = item['territory_height']
        admin_state = item['admin_state']
        url_admin_state = item['url_admin_state']
        url_admin_flag = item['url_admin_flag']
        admin_width = item['admin_width']
        admin_height = item['admin_height'] 
        lat = item['lat']
        lon = item['lon']
 
        row_territory = TEMPLATE_A_TAG.format(href=url_territory, name= territory)
        row_admin_state = TEMPLATE_A_TAG.format(href=url_admin_state, name=admin_state)
        row_territory_flag = TEMPLATE_IMG.format(src=url_territory_flag, width=territory_width, height=admin_height)
        row_admin_flag = TEMPLATE_IMG.format(src=url_admin_flag, width=admin_width, height=admin_height)
        row_coordinates = make_coordinates(lat, lon)
        row = template_row.format( territory_flag=row_territory_flag, territory=row_territory, admin_flag=row_admin_flag, admin_state=row_admin_state, coordinates=row_coordinates )

        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('un_non_self_governing_territoriescoordinates.html', 'w') as f4:
    f4.write(wdata)

