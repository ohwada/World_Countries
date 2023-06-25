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

with open('british_territories.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_teritories = dic['teritories']
    
    for item in list_teritories:
        print(item)
        teritory = item['teritory']
        url_teritory = item['url_teritory']
        capital = item['capital']
        url_capital = item['url_capital']
        url_flag = item['url_flag']
        flag_width = item['flag_width']
        flag_height = item['flag_height']
        url_arms = item['url_arms']
        arms_width = item['arms_width']
        arms_height = item['arms_height']
        location = item['location']
        motto = item['motto']
        area = item['area']     
        population = item['population']     
        gdp = item['gdp']
        gdp_per_capita = item['gdp_per_capita']
        notes = item['notes']

        row_teritory = TEMPLATE_A_TAG.format(href=url_teritory, name=teritory)
        row_capital = TEMPLATE_A_TAG.format(href=url_capital, name=capital)
        row_flag = TEMPLATE_IMG.format(src=url_flag, width=flag_width, height=flag_height)
        row_arms = TEMPLATE_IMG.format(src=url_arms, width=arms_width, height=arms_height)

        row = template_row.format(flag=row_flag, arms=row_arms, teritory=row_teritory, location=location, motto=motto, area=area, population=population, capital=row_capital, gdp=gdp, gdp_per_capita=gdp_per_capita, notes=notes )
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('british_territories.html', 'w') as f4:
    f4.write(wdata)

