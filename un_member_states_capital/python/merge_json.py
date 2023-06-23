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

with open('capitals_coordinates.json') as f1:
    dic1 = json.load(f1)
    list_countries1 = dic1['countries']

dic = {}

dic['title'] = "List of Member states of the United Nations with Capital National Flag Coordinates"

countries = []

with open('un_members_flag.json') as f2:
    dic2 = json.load(f2)
    dic['desc'] = dic2['desc']
    dic['reference'] = dic2['reference']
    dic['url_reference'] = dic2['url_reference']

    list_countries2 = dic2['countries']

    for item in list_countries2:
        d = {}
        country = item['country']
        print(country)
        url_country = item['url_country']
        d['country'] = country
        d['url_country'] = url_country
        d['url_flag_icon'] = item['url_flag_icon']
        d['icon_width'] = item['icon_width']
        d['icon_height'] = item['icon_height']
        d['url_flag'] = item['url_flag']
        d['flag_width'] = item['flag_width']
        d['flag_height'] = item['flag_height']

        is_match, matched = find_country( list_countries1, country, url_country)
        if is_match:
            capital = matched['capital']
            print(capital)
            d['capital'] = capital
            d['url_capital'] = matched['url_capital']
            d['lat'] = matched['lat']
            d['lon'] = matched['lon']
        else:
            print("not match")
            exit()
        countries.append(d)
  
dic['countries'] = countries

with open('un_members_capital.json', 'wt') as f3:
    json.dump(dic, f3)


