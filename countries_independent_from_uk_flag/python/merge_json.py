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

FORMAT_LINE = "{country}, {url_country}, {url_flag_icon}, {icon_width}, {icon_height}, {year},  {un_member},{commonwealth_nations}, {notes}\n"

wdata = ""

with open('countries_from_uk.json') as f1:
    dic1 = json.load(f1)
    list_uk_colonies = dic1['countries']

with open('commonwealth_nations.json') as f2:
    dic2 = json.load(f2)
    list_commonwealth_nations = dic2['countries']

with open('un_members_flag.json') as f3:
    dic3 = json.load(f3)
    list_un_members = dic3['countries']

for item in  list_uk_colonies:
    country = item['country']
    print(country)
    url_country = item['url_country']
    year = item['year']
    notes = item['notes']

    is_match1, matched1 = find_country(list_un_members, country, url_country)
    flag_un_member = 1 if is_match1 else 0

    is_match2, matched2 = find_country( list_commonwealth_nations, country, url_country)
    flag_commonwealth_nations = 1 if is_match2 else 0
   
    url_flag_icon = ''
    icon_width = 0
    icon_height = 0
    if is_match1:
        url_flag_icon = matched1['url_flag_icon']
        icon_width = matched1['icon_width']
        icon_height = matched1['icon_height']

    line = FORMAT_LINE.format(country=country, url_country=url_country, year=year, notes=notes,  url_flag_icon= url_flag_icon,   icon_width=  icon_width, icon_height=icon_height, un_member=flag_un_member, commonwealth_nations=flag_commonwealth_nations)
    print(line)
    wdata += line;

with open('countries_from_uk_flag.csv', 'w') as f5:
     f5.write(wdata)


