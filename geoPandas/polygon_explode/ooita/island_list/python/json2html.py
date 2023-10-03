# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'ooita_island_list.json'

FILE_HTML = 'ooita_island_list.html'

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


def make_link(name, url):
    if not url:
        return name
    atag = FORMAT_A_TAG.format(href=url, name=name)
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
list_islands = dic['islands']


for item in list_islands :
    name_en = item['name_en']
    name_island = item['name_island']
    url_island = item['url_island']
    name_municipality = item['name_municipality']
    url_municipality = item['url_municipality']
    lat = item['lat']
    lon = item['lon']
    row_island = make_link(name_island, url_island)
    row_municipality = make_link(name_municipality, url_municipality)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format(name_en=name_en, island=row_island, municipality=row_municipality, coordinates=row_coordinates)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

