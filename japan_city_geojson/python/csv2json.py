# -*- coding: utf-8 -*-
# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json


with open('japan_pref_code.json') as f1:
    dic1 = json.load(f1)
#

list_prefectures = dic1['prefectures']

FORMAT_FILENAME = 'gepjson_{code}.csv'

dic = {}

dic['title'] = 'Catalog of Japan City GeoJson'

prefs = []

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
            d['code'] = row[1].strip()
            d['kanji'] = row[2].strip()
            cities.append(d)
    pref['cities'] =  cities
    prefs.append(pref)
#

dic['prefectures'] = prefs


with open('japan_city_geocode_catalog.json', 'wt') as f3:
    json.dump(dic, f3)
#

