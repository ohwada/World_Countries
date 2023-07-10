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

FORMAT_LINE = '{territory}, {url_territory},{url_territory_flag}, {territory_width}, {territory_height}, {admin}, {url_admin}, {url_admin_flag}, {admin_width}, {admin_height}, {lat}, {lon} \n'

wdata = ""

lat = 0

lon = 0

with open('un_non_self_governing_territories.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_territories = dic['territories']
    print(str_title)
    
for item in list_territories:
    territory = item['territory']
    url_territory = item['url_territory']
    url_territory_flag = item['url_territory_flag']
    territory_width = item['territory_width']
    territory_height = item['territory_height']
    admin = item['admin_state']
    url_admin = item['url_admin_state']
    url_admin_flag = item['url_admin_flag']
    admin_width = item['admin_width']
    admin_height = item['admin_height'] 
        
    line = FORMAT_LINE.format(territory=territory, url_territory=url_territory, url_territory_flag=url_territory_flag, territory_width =territory_width, territory_height =territory_height, admin=admin, url_admin=url_admin, url_admin_flag=url_admin_flag, admin_width=admin_width, admin_height=admin_height, lat=lat, lon=lon )
    print(line)
    wdata += line;
#

with open('un_non_self_governing_territories_coordinates.csv', 'w') as f4:
    f4.write(wdata)

