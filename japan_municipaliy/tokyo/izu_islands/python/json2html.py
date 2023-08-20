# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'izu_islands_list.json'

FILE_HTML = 'izu_islands_list.html'


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
list_slands = dic['islands']


for item in list_slands :
    name_island = item['name_island']
    url_island = item['url_island']
    name_town = item['name_town']
    url_town = item['url_town']
    name_airport = item['name_airport']
    url_airport = item['url_airport']
    name_en = item['name_en']
    population = item['population']
    area = item['area']
    lat = item['lat']
    lon = item['lon']
    row_island = make_link(name_island, url_island)
    row_town = make_link(name_town, url_town)
    row_airport = make_link(name_airport, url_airport)
    row_coordinates = make_coordinates(lat, lon)
    row = template_row.format(name_en=name_en, island=row_island, town=row_town, airport=row_airport, population=population, area=area, coordinates=row_coordinates)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

