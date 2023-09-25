# download.py

import json
import os
import requests
import urllib


FILE_CATALOG = 'data/japan_prefecture_geojson_catalog.json'

DIR = 'geojson_down'


if not os.path.isdir(DIR):
    os.mkdir(DIR)
#


with open(FILE_CATALOG , 'r') as f1:
    dic1 = json.load(f1)
#

url_raw_base = dic1['url_raw_base']
list_prefectures = dic1['prefectures']


for item in list_prefectures:
    name_ja = item['name_ja']
    filename = item['filename']
    print(name_ja)
    url_geojson = urllib.parse.urljoin(url_raw_base, filename)
    save_path = os.path.join(DIR, filename)
    data = requests.get(url_geojson).content
    with open(save_path ,mode='wb') as f2:
        f2.write(data)
#
