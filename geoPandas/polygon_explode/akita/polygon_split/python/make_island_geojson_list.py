# make_island_geojson_list.py.py
# 2023-06-01 K.OHWADA

import csv
import json
import os
import shutil

FILE_LOG_CSV = 'files/split_log.csv'

FILE_ISLAND_LIST_JSON = 'data/akita_island_list.json'

FILE_LIST_CSV = 'island_geojson_list.csv'

FORMAT_LINE = '{name_en}, {name_island},  {url_island},  {name_municipality},  {url_municipality}, {filename}, {lat}, {lon} \n'

DIR_SRC = 'geojson'

DIR_DST = 'island_geojson'


if not os.path.isdir(DIR_DST):
    os.mkdir(DIR_DST)
#


places = []

with open(FILE_LOG_CSV, 'r') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 6:
            continue
        num = row[0].strip()
        lat = float( row[1].strip() )
        lon = float( row[2].strip() )
        place = row[3].strip()
        display = row[4].strip()
        filename = row[5].strip()
        d = {}
        d['place'] = place
        d[' filename'] =  filename
        places .append(d)
#


def find_place(name):
    is_match = False
    filename = ''
    for item in places:
        place = item['place']
        filename = item[' filename']
        if place == name:
            is_match = True
            break
    return[is_match,   filename]
#


def read_geojson(filepath):
    place = ''
    with open(filepath, 'r') as f:
        dic = json.load(f)
        features = dic['features']
        feature0 = features[0]
        properties = feature0['properties']
        place = properties['place']
    return place
#


with open(FILE_ISLAND_LIST_JSON, 'r') as f2:
    dic2 = json.load(f2)
#

list_islands = dic2['islands']

wdata = ''

for item in list_islands:
    name_en = item['name_en']
    name_island = item['name_island']
    url_island = item['url_island']
    name_municipality = item['name_municipality']
    url_municipality = item['url_municipality']
    lat = item['lat']
    lon = item['lon']
    print( name_island )
    if not url_island:
        continue
    is_match,   filename = find_place(name_island)
    if is_match:
        line = FORMAT_LINE.format( name_en=name_en, name_island=name_island,  url_island=url_island,  name_municipality=name_municipality,  url_municipality=url_municipality, filename=filename, lat=lat, lon=lon)
        print(line)
        wdata += line

        file_src =  os.path.join(DIR_SRC, filename)
        file_dst =  os.path.join(DIR_DST, filename)
        place = read_geojson(file_src)
        if place != name_island:
            print('unmatch', place)
            exit()
        shutil.copyfile( file_src ,  file_dst )
#


with open(FILE_LIST_CSV, 'wt') as f3:
    f3.write(wdata)
#

