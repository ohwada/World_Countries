# json2html.py
# 2023-06-01 K.OHWADA

import json

FORMAT_A_TAG = '<a href="{href}">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_ROWSPAN = 'rowspan="{rowspan}" '

def make_rowspan(rowspan):
    if rowspan == 0:
        return ''
    ret = FORMAT_ROWSPAN.format(rowspan=rowspan)
    return ret
#

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

with open('template_row_island.txt', 'r') as f3:
    template_row_island = f3.read()

teritories =[]

rows=""

with open('crown_dependencies.json') as f4:
    dic = json.load(f4)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_teritories = dic['teritories']
    print(str_title)
    
    for item in list_teritories:
        id = item['id'] 
        group = item['group']
        rowspan = item['rowspan']
        teritory = item['teritory']
        url_teritory = item['url_teritory']
        location = item['location'] 
        url_location = item['url_location'] 
        monarch = item['monarch'] 
        url_monarch = item['url_monarch']
        area = item['area']
        population = item['population']
        url_flag = item['url_flag'] 
        flag_width = item['flag_width'] 
        flag_height = item['flag_height'] 
        url_arms =  item['url_arms'] 
        arms_width = item['arms_width']
        arms_height = item['url_arms_height']
        capital =  item['capital']
        url_capital =  item['url_capital']
        airport = item['airport'] 
        url_airport = item['url_airport'] 

        row_teritory = FORMAT_A_TAG.format(href= url_teritory, name=teritory)
        row_location = FORMAT_A_TAG.format(href= url_location, name=location)
        row_monarch = FORMAT_A_TAG.format(href= url_monarch, name=monarch)
        row_capital = FORMAT_A_TAG.format(href= url_capital, name=capital)
        row_airport = FORMAT_A_TAG.format(href= url_airport, name=airport)
        row_flag = FORMAT_IMG.format(src= url_flag, width=flag_width, height=flag_height )
        row_arms = FORMAT_IMG.format(src= url_arms, width=arms_width, height=arms_height )
        row_rowspan = make_rowspan(rowspan)

        if group == 0:
            row = template_row.format( teritory=row_teritory, location = row_location, monarch=row_monarch, area=area, population=population, flag=row_flag, arms=row_arms, capital=row_capital, airport=row_airport, rowspan=row_rowspan)
        else: 
            row = template_row_island.format( flag=row_flag, arms=row_arms, capital=row_capital, airport=row_airport )
        print(row)
        rows +=  row
#

html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('crown_dependencies.html', 'w') as f5:
    f5.write(wdata)

