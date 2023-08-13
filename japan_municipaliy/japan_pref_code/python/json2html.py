# -*- coding: utf-8 -*-
# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'japan_prefecture_code_list.json'

FILE_HTML  = 'japan_prefecture_code_list.html'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'



with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#


with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#


rows = ''

with open(FILE_JSON, 'r') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    title_ja = dic['title_ja']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_prefectures = dic['prefectures']
  #
 
html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

for item in list_prefectures :
    code = item['code']
    name_en = item['name_en']
    name_ja = item['name_ja']
    row = template_row.format( code=code, name_en=name_en, name_ja=name_ja)
    print(row)
    rows +=  row
#

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

