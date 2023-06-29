# json2csv.py
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

FORMAT_LINE = '{teritory}, {url_teritory},{url_teritory_flag}, {teritory_width}, {teritory_height}, {admin}, {url_admin}, {url_admin_flag}, {admin_width}, {admin_height}, {lat}, {lon} \n'

wdata = ""

lat = 0

lon = 0

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
    admin = item['admin_state']
    url_admin = item['url_admin_state']
    url_admin_flag = item['url_admin_flag']
    admin_width = item['admin_width']
    admin_height = item['admin_height'] 
        
    line = FORMAT_LINE.format(teritory=teritory, url_teritory=url_teritory, url_teritory_flag=url_teritory_flag, teritory_width =teritory_width, teritory_height =teritory_height, admin=admin, url_admin=url_admin, url_admin_flag=url_admin_flag, admin_width=admin_width, admin_height=admin_height, lat=lat, lon=lon )
    print(line)
    wdata += line;
#

with open('un_non_self_governing_territories_coordinates.csv', 'w') as f4:
    f4.write(wdata)

