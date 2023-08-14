# json2html.py
# 2023-06-01 K.OHWADA

import json


FORMAT_A_TAG = '<a href="{href}">{name}</a> '

FORMAT_TABLE_TTITLE = '{code} : {name}'

FORMAT_CONTENT = '<li><a href="#{code}">{name}</a></li>'

FORMAT_CONTENTS = '<ul>{contents}</ul>'


def make_link(url_base, filepath):
    href = url_base + filepath
    link= FORMAT_A_TAG.format(href=href, name=filepath)
    return link
#


def make_row(url_base, item):
    filepath = item2['filepath']
    n001 = item2['N03_001']
    n002 = item2['N03_002']     
    n003 = item2['N03_003']      
    n004 = item2['N03_004']
    n007 = item2['N03_007']
    link = make_link(url_base, filepath)
    row = template_row.format( n001=n001, n002=n002, n003=n003, n004=n004, n007=n007, filepath=link)
    return row
#


with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('files/template_table.txt', 'r') as f2:
    template_table = f2.read()
#

with open('files/template_row.txt', 'r') as f3:
    template_row = f3.read()
#

rows = ''

with open('japan_city_geojson_catalog.json') as f4:
    dic = json.load(f4)
#

title_ja = dic['title_ja']

url_base = dic['url_base']

ref = dic['reference']

url_ref = dic['url_reference']

list_prefectures = dic['prefectures']

contents = ''

tables = ''

for item1 in list_prefectures :
    pref_code = item1['code']
    pref_name = item1['name_ja']
    list_cities = item1['cities']
    table_title = FORMAT_TABLE_TTITLE .format(code=pref_code, name=pref_name)
    rows = ''

    for item2 in list_cities :
        row = make_row(url_base, item2)
        print(row)
        rows +=  row
    table = template_table.format(table_title=table_title, code=pref_code, rows=rows)
    tables += table
    content = FORMAT_CONTENT.format(code=pref_code,name=table_title)
    contents  += content 
#


html_contents = FORMAT_CONTENTS.format(contents=contents)

html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, tables= tables, contents=html_contents, reference=html_ref)
  

with open('japan_city_geojson_catalog.html', 'w') as f5:
    f5.write(wdata)
#

