# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_CODE ='japan_prefecture_code_list.json'

FILE_DETAIL = 'data/japan_prefecture_detail_list.json'

FILE_CSV = 'japan_prefecture_list.csv'


FORMAT_LINE = '{code}, {name_en}, {name_pref}, {url_pref}, {name_capital}, {url_capital}, {url_icon}, {icon_width}, {icon_height}, {url_flag}, {flag_width}, {flag_height}, {lat} , {lon} \n'


with open(FILE_DETAIL, 'r') as f1:
    dic1 = json.load(f1)
#


list_prefectures1 = dic1['prefectures']


def find_pref(pref_code, pref_name):
    is_match = False
    matched = None
    for item in list_prefectures1:
        item_code = item['code']
        item_pref = item['name_pref']
        if item_code == pref_code:
            is_match = True
            matched = item
            break
        if item_pref == pref_name:
            is_match = True
            matched = item
            break
    return [ is_match,      matched]
#


with open(FILE_CODE, 'r') as f2:
    dic2 = json.load(f2)
#


list_prefectures2 = dic2['prefectures']


wdata = ''


for item2 in list_prefectures2 :
    code = item2['code']
    kanji = item2['kanji']
    name_en = item2['name']
    url_flag = item2['url_flag']
    flag_width = item2['flag_width']
    flag_height = item2['flag_height']
    lat = item2['lat']
    lon = item2['lon']
    is_match, matched = find_pref(code, kanji)
    if is_match:
        name_pref = matched['name_pref']
        url_pref = matched['url_pref']
        name_capital = matched['name_capital_city']
        url_capital = matched['url_capital_city']
        url_icon = matched['url_flag']
        icon_width = matched['flag_width']
        icon_height = matched['flag_height']

    line = FORMAT_LINE.format(code=code, name_en=name_en, name_pref=name_pref, url_pref=url_pref, name_capital=name_capital, url_capital=url_capital, url_icon=url_icon, icon_width=icon_width, icon_height=icon_height, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height, lat=lat, lon=lon)
    print(line)
    wdata +=  line
#


with open(FILE_CSV, 'wt') as f2:
    f2.write(wdata)
#

