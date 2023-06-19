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

with open('un_countries_flag.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    print(str_title)
    
    for item in list_countries:
        country = item['country']
        offical_name = item['offical_name']
        url_country = item['url_country']
        url_flag_icon = item['url_flag_icon']
        icon_width = item['icon_width']
        icon_height = item['icon_height']
        url_flag = item['url_flag']
        flag_width = item['flag_width']
        flag_height = item['flag_height']
        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        h = int( (WIDTH * flag_height) / flag_width )
        row_flag = TEMPLATE_IMG.format(src=url_flag, width=WIDTH, height=h)
        row_flag_icon = TEMPLATE_IMG.format(src=url_flag_icon, width=icon_width, height=icon_height)
        row = template_row.format(country=row_country, name= offical_name, flag=row_flag, flag_icon=row_flag_icon)
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('un_countries_flag.html', 'w') as f4:
    f4.write(wdata)

