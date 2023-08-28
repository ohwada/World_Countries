# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'kanagawa_area_list.json'


FILE_HTML = 'kanagawa_area_list.html'


FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'


FORMAT_CONTENT = '<li><a href="#{code}">{name}</a></li> \n'

FORMAT_CONTENTS = '<ul>{contents}</ul>'


FORMAT_REFS = '<ul><li>{ref1}</li><li>{ref2}</li></ul>'

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


with open('files/template_table.txt', 'r') as f3:
    template_table = f3.read()
#



with open(FILE_JSON, 'r') as f4:
    dic = json.load(f4)
#

title_ja = dic['title_ja']

ref1 = dic['reference1']

url_ref1 = dic['url_reference1']

ref2 = dic['reference2']

url_ref2 = dic['url_reference2']

list_areas = dic['areas']

contents = ''

tables = ''

for item1 in list_areas :
    name_area_en = item1['name_en']
    name_area = item1['name_area']
    url_area = item1['url_area']
    list_cities = item1['cities']
    content = FORMAT_CONTENT.format(code=name_area_en, name=name_area)
    contents +=   content  
    rows = ''

    for item2 in list_cities :
        group = item2['group']
        name_city_en = item2['name_en']
        name_city = item2['name_city']
        url_city = item2['url_city']
        row_city = FORMAT_A_TAG.format(href=url_city, name=name_city)
        row = template_row.format(group=group, name_en=name_city_en, city=row_city)
        print(row)
        rows +=  row

    table = template_table.format(table_name =name_area_en, table_title=name_area, rows=rows)
    tables += table
#


html_contents = FORMAT_CONTENTS.format(contents=contents)
   

html_ref1 = FORMAT_A_TAG.format(href=url_ref1, name=ref1)

html_ref2 = FORMAT_A_TAG.format(href=url_ref2, name=ref2)

html_ref = FORMAT_REFS.format(ref1=html_ref1, ref2=html_ref2)

wdata = template_html.format(body_title=title_ja, contents=html_contents, reference=html_ref, tables=tables)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

