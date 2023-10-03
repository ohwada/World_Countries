# check.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'kagawa_island_list.json'

FILE_TARGET = 'kagawa_island_list_target.json'

FILE_CSV = 'island_list.csv'

FORMAT_LINE = '{name_en}, {name_island},  {url_island},  {name_municipality},  {url_municipality}, {lat}, {lon} \n'


with open(FILE_JSON, 'r') as f1:
    dic1 = json.load(f1)
#

list_islands_1 = dic1['islands']

def find_island(name_en, name_island):
    is_match = False
    for item in list_islands_1:
        item_name_en = item['name_en']
        item_name_island = item['name_island']
        if item_name_en == name_en:
            is_match = True
            break
        if item_name_island == name_island:
            is_match = True
            break
    return is_match
#


with open(FILE_TARGET, 'r') as f2:
    dic2 = json.load(f2)
#

list_islands_2 = dic2['islands']

wdata = ''


for item2 in list_islands_2:
    name_en = item2['name_en']
    name_island = item2['name_island']
    url_island = item2['url_island']
    if url_island == '':
        url_island = '-'
    name_municipality = item2['name_municipality']
    url_municipality = item2['url_municipality']
    lat = item2['lat']
    lon = item2['lon']
    is_match = find_island(name_en, name_island)
    if not is_match:    
        line = FORMAT_LINE.format(name_en=name_en,  name_island=name_island,  url_island= url_island, name_municipality = name_municipality, url_municipality=url_municipality, lat=lat, lon=lon) 
        print(line)
        wdata += line
#


with open(FILE_CSV, 'wt') as f3:
    f3.write(wdata)
#
