# json2csvpy
# 2023-06-01 K.OHWADA

import json

FORMAT_LINE = '{id}, {group}, {rowspan},{territory}, {url_territory}, {url_flag}, {flag_width}, {flag_height}, {capital}, {url_capital}, {island}, {url_island}, {lat}, {lon} \n'

with open('crown_dependencies.json') as f1:
    dic = json.load(f1)
    list_islands = dic['islands']
#

island = '-'
url_island = '-'
lat = 0
lon = 0
wdata= ''

for item in list_islands:
    id= item['id']
    group = item['group']
    rowspan = item['rowspan']
    territory = item['territory']
    url_territory = item['url_territory']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    capital = item['capital']
    url_capital = item['url_capital']

    line = FORMAT_LINE.format( id=id, group=group, rowspan=rowspan, territory=territory, url_territory=url_territory, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height,   capital=capital, url_capital=url_capital, island=island, url_island=url_island, lat=lat, lon=lon )

    wdata += line
#

with open('crown_dependencies_coordinates.csv', 'w') as f2:
    f2.write(wdata)

