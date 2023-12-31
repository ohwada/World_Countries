# merge_jsonpy
# 2023-06-01 K.OHWADA

import json

COMMA = ','

COMMA_HTML = '&comma;'

def replace_comma_html(data):
    if not data:
        return ''
    ret = data.replace(COMMA, COMMA_HTML)
    return ret
#

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

FORMAT_LINE = "{country}, {url_country}, {capital}, {url_capital}, {url_flag_icon}, {icon_width}, {icon_height}, {lat}, {lon} \n"

wdata = ""

with open('countries_from_uk.json') as f1:
    dic1 = json.load(f1)
    list_countries = dic1['countries']

with open('un_members_capital.json') as f2:
    dic2 = json.load(f2)
    list_un_members = dic2['countries']

with open('countries_from_uk_dominion.json') as f3:
    dic3 = json.load(f3)
    list_dominion = dic3['countries']

for item in  list_countries:
    country = item['country']
    print(country)
    url_country = item['url_country']
    url_flag_icon = item['url_flag_icon']
    icon_width = item['icon_width']
    icon_height = item['icon_height']

    is_match, matched = find_country(list_un_members, country, url_country)
 
    capital = '-'
    url_capital = '-'
    lat = 0
    lon = 0
    if is_match:
        capital = replace_comma_html( matched['capital'] )
        url_capital =  matched['url_capital']
        lat = matched['lat']
        lon = matched['lon']

    line = FORMAT_LINE.format(country=country, url_country=url_country, capital=capital, url_capital=url_capital, url_flag_icon= url_flag_icon,   icon_width=  icon_width, icon_height=icon_height, lat=lat, lon=lon)
    print(line)
    wdata += line;
#



for item in  list_dominion:
    country = item['country']
    print(country)
    url_country = item['url_country']
    url_flag_icon = item['url_flag_icon']
    icon_width = item['icon_width']
    icon_height = item['icon_height']

    is_match, matched = find_country(list_un_members, country, url_country)
 
    capital = '-'
    url_capital = '-'
    lat = 0
    lon = 0
    if is_match:
        capital = replace_comma_html( matched['capital'] )
        url_capital =  matched['url_capital']
        lat = matched['lat']
        lon = matched['lon']

    line = FORMAT_LINE.format(country=country, url_country=url_country, capital=capital, url_capital=url_capital, url_flag_icon= url_flag_icon,   icon_width=  icon_width, icon_height=icon_height, lat=lat, lon=lon)
    print(line)
    wdata += line;
#

with open('countries_from_uk_capital.csv', 'w') as f5:
     f5.write(wdata)


