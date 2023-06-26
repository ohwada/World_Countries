# merge_jsonpy
# 2023-06-01 K.OHWADA

import json

def find_country( list_countries, country, url_country):
    for item in  list_countries:
        item_country = item['country']
        item_url_country = item['url_country']
        is_match = False
        if   country == item_country:
            is_match = True
            matched = item
            break
        if   url_country == item_url_country:
            is_match = True
            matched = item
            break

    if is_match:
        return[True, matched]
    else:
        return[False, None]
#

TITLE = 'List of Member states of the Commonwealth of Nations with Nationnal Flag icon'

with open('un_members_flag.json') as f1:
    dic1 = json.load(f1)
    list_un_members = dic1['countries']

with open('commonwealth_nations.json') as f2:
    dic2 = json.load(f2)
    list_commonwealth_nations = dic2['countries']
    
countries = []

for item in  list_commonwealth_nations:
    country = item['country']
    url_country = item['url_country']
    print(country)
    is_match, matched = find_country(    list_un_members , country, url_country)
    url_flag_icon =  ''
    icon_width =  0
    icon_height =  0
    if is_match:
        url_flag_icon =  matched['url_flag_icon']
        icon_width =  matched['icon_width']
        icon_height =  matched['icon_height']
    item['url_flag_icon'] = url_flag_icon
    item['icon_width'] = icon_width
    item['icon_height'] = icon_height
    countries.append(item)
#

dic2['title'] = TITLE

dic2['countries'] = countries

with open('commonwealth_nations_flag.json', 'w') as f3:
      json.dump(dic2, f3)


