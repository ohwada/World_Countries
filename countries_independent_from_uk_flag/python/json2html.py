# json2html.py
# 2023-06-01 K.OHWADA

import json

def conv_yn(data):
    yn= 'Yes' if data ==1 else 'No'
    return yn
#

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

WIDTH = 100

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

countries =[]

rows=""

with open('countries_from_uk_flag.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
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
        year = item['year']
        un_member = conv_yn( item['un_member'] )
        commonwealth_nations = conv_yn( item['commonwealth_nations'] )
        notes = item['notes']

        row_country = TEMPLATE_A_TAG.format(href=url_country, name=country)
        row_flag_icon = TEMPLATE_IMG.format(src=url_flag_icon, width=icon_width, height=icon_height)
        row = template_row.format(country=row_country, flag_icon= row_flag_icon, year=year, un_member =un_member ,  commonwealth_nations= commonwealth_nations,  notes=notes)
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('countries_from_uk_flag.html', 'w') as f4:
    f4.write(wdata)

