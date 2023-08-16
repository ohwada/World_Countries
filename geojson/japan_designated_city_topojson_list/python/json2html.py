# json2html.py
# 2023-06-01 K.OHWADA

import json
import urllib.parse


FILE_CATALOG = 'designated_cities_topojson_catalog.json'

FILE_HTML = 'designated_cities_topojson_catalog.html'

FORMAT_A_TAG = '<a href="{href}">{name}</a> '

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

FORMAT_REFERENCE =  '<li><a href="{href}">{name}</a></li> \n'

FORMAT_REFERENCES =  '<ul>{references}</ul>'

ZOOM = 10


def make_link(url_base, filepath):
    url_topojson = urllib.parse.urljoin(url_base, filepath)
    link= FORMAT_A_TAG.format(href=url_topojson, name=filepath)
    return link
#


def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon = FORMAT_LATLON.format( lat=lat, lon=lon )
    atag = FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#

def make_row(url_base, item):
    n001 = item['N03_001']
    n003 = item['N03_003']         
    n007 = item['N03_007']
    id = item['id']
    filepath = item['filepath']
    name = item['name']
    lat = item['lat']
    lon = item['lon']
    link = make_link(url_base, filepath)
    coordinates = make_coordinates(lat, lon)
    row = template_row.format( name=name, n001=n001, n003=n003, n007=n007, id=id, filepath=link, coordinates=coordinates)
    return row
#


with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#


with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open(FILE_CATALOG, 'r') as f3:
    dic = json.load(f3)
#

title_ja = dic['title_ja']

url_base = dic['url_base']

ref1 = dic['reference1']

url_ref1 = dic['url_reference1']

ref2 = dic['reference2']

url_ref2 = dic['url_reference2']

list_cities = dic['cities']

for item1 in list_cities :
    row = make_row(url_base, item1)
    print(row)
    rows +=  row
#

html_ref1 = FORMAT_REFERENCE.format(href=url_ref1, name=ref1)

html_ref2 = FORMAT_REFERENCE.format(href=url_ref2, name=ref2)

refs = html_ref1 + html_ref2

html_refs = FORMAT_REFERENCES.format( references=refs)


wdata = template_html.format(body_title=title_ja, rows= rows, references=html_refs)
  

with open(FILE_HTML, 'wt') as f5:
    f5.write(wdata)
#

