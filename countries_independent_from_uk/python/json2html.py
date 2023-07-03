# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

WIDTH = 100

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

countries =[]

rows=""

with open('countries_from_uk.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    table_title = dic['table_title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    print(str_title)
    
    for item in list_countries:
        country = item['country']
        url_country = item['url_country']
        url_flag_icon = item['url_flag_icon']
        icon_width = item['icon_width']
        icon_height = item['icon_height']
        pre_name = item['pre_name']
        date = item['date']
        year = item['year']
        notes = item['notes']

        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        row_flag = TEMPLATE_IMG.format(src=url_flag_icon, width=icon_width, height=icon_height )
        row = template_row.format(country=row_country, flag_icon=row_flag, pre_name= pre_name, date=date, year=year, notes=notes)
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, table_title=table_title, desc = desc, reference=html_ref, rows=rows)
  
with open('countries_from_uk.html', 'w') as f4:
    f4.write(wdata)

