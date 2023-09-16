# download.py
# 2023-06-01 K.OHWADA

import os
import json
import requests
import urllib

FILE_CITY_LIST = 'data/japan_ordinance_designated_city_list.json'

FILE_CATALOG = 'data/japan_city_geojson_catalog.json'

DIR = 'geojson'

if not os.path.isdir(DIR):
    os.mkdir(DIR)


with open( FILE_CITY_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_cities1 = dic1['cities']


with open(FILE_CATALOG, 'r') as f2:
    dic2 = json.load(f2)
#

url_raw_base = dic2['url_raw_base']
list_prefectures = dic2['prefectures']

parent_names = []

for item1 in list_cities1:
    name_ja = item1['name_ja']
    print(name_ja)
    parent_names.append(name_ja)
#


for item2 in list_prefectures:
    pref_kanji = item2['kanji']
    list_cities2 = item2['cities']
    print(pref_kanji)
    for item3 in list_cities2:
        parent_name = item3['N03_003']
        city_name = item3['N03_004']
        filepath = item3['filepath']
        print(parent_name)
        url_geojson = urllib.parse.urljoin(url_raw_base, filepath)
        basename = os.path.basename(filepath)
        save_path = os.path.join(DIR, basename)
        is_parent = parent_name in parent_names
        if  is_parent:
            print(city_name)
            data = requests.get(url_geojson).content
            with open(save_path ,mode='wb') as f3:
                f3.write(data)


