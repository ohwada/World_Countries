# json2html.py
# 2023-06-01 K.OHWADA

import json


FORMAT_REF = '<li><a href="{href}">{name}</a></li>'

FORMAT_REFS = '<ul>{refs}</ul>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open('japan_pref_code.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    title_ja = dic['title_ja']
    ref1 = dic['reference1']
    url_ref1 = dic['url_reference1']
    ref2 = dic['reference2']
    url_ref2 = dic['url_reference2']
    list_prefectures = dic['prefectures']
  #
 
ref1 = FORMAT_REF.format(href=url_ref1, name=ref1)

ref2 = FORMAT_REF.format(href=url_ref2, name=ref2)

refs = ref1 + ref2

html_refs = FORMAT_REFS.format(refs=refs)

for item in list_prefectures :
    code = item['code']
    name = item['name']
    kanji = item['kanji']
    kana= item['kana']
    row = template_row.format( code=code, name=name, kanji=kanji, kana=kana)

    print(row)
    rows +=  row
#

wdata = template_html.format(body_title=title_ja, reference=html_refs, rows=rows)
  
with open('japan_prefectures_code.html', 'w') as f4:
    f4.write(wdata)
#

