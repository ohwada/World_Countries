# json2csv.py
# 2023-06-01 K.OHWADA

import json

FILE_CITY_LIST = 'data/kanagawa_city_flag_list.json'

FILE_TOWN_LIST = 'data/kanagawa_town_flag_list.json'

FILE_CSV = 'kanagawa_city_flag_list.csv'

FORMAT_LINE = '{group}, {name_city}, {url_city}, {url_flag}, {flag_width}, {flag_height} \n'



def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#


wdata = ''

with open(FILE_CITY_LIST, 'r') as f1:
    dic1 = json.load(f1)
#

list_cities = dic1['cities']

group = 2


for item in list_cities :
    name_city = item['name_city']
    url_city = item['url_city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']

    line = FORMAT_LINE.format(group=group, name_city=name_city, url_city=url_city, url_flag=url_flag, flag_width=flag_width,  flag_height= flag_height )
    print(line)
    wdata += line
#


with open(FILE_TOWN_LIST, 'r') as f2:
    dic2 = json.load(f2)
#

list_towns = dic2['towns']

group = 3


for item in list_towns :
    name_town = item['name_town']
    url_town = item['url_town']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']

    line = FORMAT_LINE.format(group=group, name_city=name_town, url_city=url_town, url_flag=url_flag, flag_width=flag_width,  flag_height= flag_height )
    print(line)
    wdata += line
#


with open(FILE_CSV, 'wt') as f3:
    f3.write(wdata)
#

