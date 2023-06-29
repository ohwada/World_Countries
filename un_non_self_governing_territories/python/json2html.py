# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

def make_a_tag(name, href):
    if not href:
        return name
    ret = TEMPLATE_A_TAG.format(href=href, name=name)
    return ret
#


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

teritories =[]

rows=""

with open('un_non_self_governing_territories.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_teritories = dic['teritories']
    print(str_title)
    
    for item in list_teritories:
        teritory = item['teritory']
        url_teritory = item['url_teritory']
        url_teritory_flag = item['url_teritory_flag']
        teritory_width = item['teritory_width']
        teritory_height = item['teritory_height']
        admin_state = item['admin_state']
        url_admin_state = item['url_admin_state']
        url_admin_flag = item['url_admin_flag']
        admin_width = item['admin_width']
        admin_height = item['admin_height'] 
        domestic_legal_status = item['domestic_legal_status']
        url_domestic_legal_status = item['url_domestic_legal_status']
        other_claimant = item['other_claimant']
        url_other_claimant = item['url_other_claimant']
        population =  item['population']
        area = item['area']
        referendum = item['referendum']
        note = item['note']
        url_note = item['url_note'] 

        row_teritory = TEMPLATE_A_TAG.format(href=url_teritory, name= teritory)
        row_admin_state = TEMPLATE_A_TAG.format(href=url_admin_state, name=admin_state)
        row_teritory_flag = TEMPLATE_IMG.format(src=url_teritory_flag, width=teritory_width, height=admin_height)
        row_admin_flag = TEMPLATE_IMG.format(src=url_admin_flag, width=admin_width, height=admin_height)
        row_domestic_legal_status = TEMPLATE_A_TAG.format(href=url_domestic_legal_status, name=domestic_legal_status)
        row_claimant = make_a_tag(other_claimant, href=url_other_claimant)

        row_note = TEMPLATE_A_TAG.format(href=url_note, name=note)

        row = template_row.format( teritory_flag=row_teritory_flag, teritory=row_teritory, admin_flag=row_admin_flag, admin_state=row_admin_state, domestic_legal_status=row_domestic_legal_status, claimant=row_claimant, population=population, area=area, referendum=referendum, note = row_note )

        print(row)
        rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('un_non_self_governing_territories.html', 'w') as f4:
    f4.write(wdata)

