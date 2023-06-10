# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

with open('template_whole.txt', 'r') as f1:
    template_whole = f1.read()

with open('template_table.txt', 'r') as f2:
    template_table = f2.read()

with open('template_row.txt', 'r') as f3:
    template_row = f3.read()

countries =[]

rows=""

with open('capitals.json') as f4:
    dic = json.load(f4)
    str_title = dic['title']
    desc = dic['desc']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    print(str_title)
    
    for item in list_countries:
        country = item['country']
        url_country = item['url_country']
        capital = item['capital']
        url_capital = item['url_capital']
        url_flag = item['url_flag']
        width = item['width']
        height = item['height']
        notes = item['notes']
        print(country)
        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        print( row_country)
        row_capital = TEMPLATE_A_TAG.format(href=url_capital, name=capital)
        row_flag = TEMPLATE_IMG.format(src=url_flag, width=width, height=height)
        row = template_row.format(flag=row_flag, country=row_country, capital=row_capital, notes=notes)
        print(row)
        rows +=  row

whole_countries = template_table.format(rows=rows)
print(whole_countries)

wdata = template_whole.format(body_title=str_title, desc = desc, url_ref=url_ref, countries=whole_countries)
  
with open('capitals.html', 'w') as f5:
    f5.write(wdata)

