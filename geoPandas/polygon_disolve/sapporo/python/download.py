# download.py
# 2023-06-01 K.OHWADA

import os
import json
import requests
import urllib

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

PREF = '北海道'

PARENT = '札幌市'

DIR = 'geojson_down'

if not os.path.isdir(DIR):
    os.mkdir(DIR)


with open(FILE_CATALOG, 'r') as f1:
    dic1 = json.load(f1)
#

url_raw_base = dic1['url_raw_base']
list_prefectures = dic1['prefectures']


for item1 in list_prefectures:
    pref_kanji = item1['kanji']
    list_cities2 = item1['cities']
    print(pref_kanji)
# Hokkaido ?
    if pref_kanji != PREF:
        continue
    for item2 in list_cities2:
        parent_name = item2['N03_003']
        city_name = item2['N03_004']
        filepath = item2['filepath']
        print(parent_name)
        url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
        basename = os.path.basename(filepath)
        save_path = os.path.join(DIR, basename)
# Sapporo ?
        if parent_name == PARENT:
            print(city_name)
            data = requests.get(url_geojson).content
            with open(save_path ,mode='wb') as f2:
                f2.write(data)
#

