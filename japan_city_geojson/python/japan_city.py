# -*- coding: utf-8 -*-
#  japan_city.py
# 2023-06-01 K.OHWADA

import csv
import json

FILE_PREF_JSON = 'data/japan_prefecture_code_list.json'

FILE_CATALOG_JSON = 'japan_city_geojson_catalog.json'

FORMAT_FILENAME = 'csv/gepjson_{code}.csv'

dic = {}

dic['title'] = 'Catalog of Japan City GeoJson'

dic['title_ja'] = '市区町村の GeoJson の一覧'

dic['url_base'] = 'https://github.com/niiyz/JapanCityGeoJson/blob/master/'

dic['url_raw_base'] = 'https://raw.githubusercontent.com/niiyz/JapanCityGeoJson/master/'

dic['reference'] = 'Japan City GeoJson 2020'

dic['url_reference'] = 'https://github.com/niiyz/JapanCityGeoJson'

prefs = []


with open(FILE_PREF_JSON, 'r') as f1:
    dic1 = json.load(f1)
#

list_prefectures = dic1['prefectures']

for item in list_prefectures:
    pref = item
    pref_code = item['code']
    filename = FORMAT_FILENAME.format(code=pref_code)
    cities = []
    with open(filename) as f2:
        reader = csv.reader(f2)

        for row in reader:
            d = {}
            d['filepath'] = row[0].strip()
            d['N03_001'] = row[1].strip()
            d['N03_002'] = row[2].strip()
            d['N03_003'] = row[3].strip()
            d['N03_004'] = row[4].strip()
            d['N03_007'] = row[5].strip()

            cities.append(d)
    pref['cities'] =  cities
    prefs.append(pref)
#

dic['prefectures'] = prefs



with open(FILE_CATALOG_JSON, 'wt',  encoding='utf-8') as f3:
    json.dump(dic, f3, ensure_ascii=False)


#

