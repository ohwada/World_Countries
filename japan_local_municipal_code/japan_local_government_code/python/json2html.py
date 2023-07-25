# json2html.py
# 2023-06-01 K.OHWADA

import json

FORMAT_A_TAG = '<a href="{href}">{name}</a>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open('japan_local_government_code.json') as f3:
    dic = json.load(f3)
    title_ja = dic['title_ja']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_cities = dic['cities']
  #
 
html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

for item in list_cities :
    code = item['code']
    pref_kanji = item['pref_kanji']
    city_kanji = item['city_kanji']
    pref_kana= item['pref_kana']
    city_kana = item['city_kana']

    row = template_row.format( code=code, pref_kanji=pref_kanji, city_kanji=city_kanji, pref_kana=pref_kana, city_kana=city_kana)

    print(row)
    rows +=  row
#

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open('japan_local_government_code.html', 'w') as f4:
    f4.write(wdata)
#

