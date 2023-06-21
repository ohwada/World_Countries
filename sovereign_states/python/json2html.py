# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

countries =[]

rows=""

with open('sovereign_states.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    print(str_title)
    
    for item in list_countries:
        country = item['country']
        formal_name = item['formal_name']
        url_country = item['url_country']
        url_flag = item['url_flag']
        width = item['width']
        height = item['height']
        membership = item['membership']
        dispute = item['dispute']
        info = item['info']
        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        row_flag = TEMPLATE_IMG.format(src=url_flag, width=width, height=height)
        row = template_row.format(flag=row_flag, country=row_country,  formal_name=formal_name, membership = membership, dispute=dispute, info=info)
        print(row)
        rows +=  row

reference = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference = reference, rows=rows)
  
with open('sovereign_states.html', 'w') as f4:
    f4.write(wdata)

