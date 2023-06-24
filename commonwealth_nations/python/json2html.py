# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

def make_link(name, url):
    if not url:
        return name
    a_tag = TEMPLATE_A_TAG.format(href=url, name=name)
    return a_tag
#

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

countries =[]

rows=""

with open('commonwealth_nations.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    
    for item in list_countries:
        country = item['country']
        url_country = item['url_country']
        date = item['date']
        region = item['region']
        url_region = item['url_region']
        subregion = item['subregion']
        url_subregion = item['url_subregion']
        population = item['population']
        government = item['government']
        notes = item['notes']

        row_country =  make_link(country, url_country)
        row_region =  make_link(region, url_region)
        row_subregion =  make_link(subregion, url_subregion)
        row = template_row.format(country=row_country, date=date, region=row_region, subregion=row_subregion, population=population, government=government,notes=notes)
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('commonwealth_nations.html', 'w') as f4:
    f4.write(wdata)

