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

with open('commonwealth_realm.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_countries = dic['countries']
    
    for item in list_countries:
        country = item['country']
        url_country = item['url_country']
        population = item['population']
        year = item['year']
        governor = item['governor']
        url_governor = item['url_governor']
        prime_minister = item['prime_minister']
        url_prime_minister = item['url_prime_minister']

        row_country =  make_link(country, url_country)
        row_governor =  make_link( governor, url_governor)
        row_prime_minister =  make_link(prime_minister, url_prime_minister)
        row = template_row.format(country=row_country, population=population, year=year, governor=row_governor, prime_minister=row_prime_minister)
        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('commonwealth_realm.html', 'w') as f4:
    f4.write(wdata)

