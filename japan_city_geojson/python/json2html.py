# json2html.py
# 2023-06-01 K.OHWADA

import json


FORMAT_TABLE_TTITLE = '{code} : {name}'

FORMAT_CONTENT = '<li><a href="#{code}">{name}</a></li>'

FORMAT_CONTENTS = '<ul>{contents}</ul>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_table.txt', 'r') as f2:
    template_table = f2.read()
#

with open('template_row.txt', 'r') as f3:
    template_row = f3.read()
#

rows = ''

with open('japan_city_geocode_catalog.json') as f4:
    dic = json.load(f4)
#

str_title = dic['title']
list_prefectures = dic['prefectures']

contents = ''

tables = ''

for item1 in list_prefectures :
    pref_code = item1['code']
    pref_kanji = item1['kanji']
    list_cities = item1['cities']
    table_title = FORMAT_TABLE_TTITLE .format(code=pref_code, name=pref_kanji)
    rows = ''

    for item2 in list_cities :
        city_code = item2['code']
        city_kanji = item2['kanji']
        city_filepath = item2['filepath']
        row = template_row.format( code=city_code, name=city_kanji, filepath=city_filepath)
        print(row)
        rows +=  row
    table = template_table.format(table_title=table_title, code=pref_code, rows=rows)
    tables += table
    content = FORMAT_CONTENT.format(code=pref_code,name=table_title)
    contents  += content 
#

html_contents = FORMAT_CONTENTS.format(contents=contents)

wdata = template_html.format(body_title=str_title, tables= tables, contents=html_contents)
  
with open('japan_city_geocode.html', 'w') as f5:
    f5.write(wdata)
#

