# json2html.py
# 2023-06-01 K.OHWADA

import json

TITLE = 'JIS X 0401 都道府県コード'

FILE_JSON = 'data/JISX0401_Prefecture_list.json'

FILE_HTML = 'prefecture_list.html'


REF = 'JIS X 0401 都道府県コード JSON'

URL_REF = 'https://qiita.com/HirMtsd/items/5de2ee19e086f07921d2'

FORMAT_A_TAG = '<a href="{href}">{name}</a>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open(FILE_JSON, 'r') as f3:
    dic = json.load(f3)
#

list_prefectures = dic['prefectures']
 

for item in list_prefectures :
    code = item['code']
    en_name = item['en_name']['ja']
    kanji_name = item['name']
    kana_name= item['kana_name']['full_lower']    
    start_date = item['start_date']
    row = template_row.format( code=code, en_name=en_name, kanji_name=kanji_name, kana_name=kana_name, start_date=start_date)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=URL_REF, name=REF)

wdata = template_html.format(body_title=TITLE, reference=html_ref, rows=rows)
  
with open(FILE_HTML , 'wt') as f4:
    f4.write(wdata)
#

