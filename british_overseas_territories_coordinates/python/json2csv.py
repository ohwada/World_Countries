# json2csvpy
# 2023-06-01 K.OHWADA

import json

FORMAT_LINE = '{territory}, {url_territory},  {capital}, {url_capital}{url_flag}, {flag_width}, {flag_height}, {lat}, {lon} \n'


with open('british_overseas_territories.json') as f1:
    dic = json.load(f1)
    list_territories = dic['territories']
#

lat = 0
lon = 0
wdata= ''

for item in list_territories:
    territory = item['territory']
    url_territory = item['url_territory']
    capital = item['capital']
    url_capital = item['url_capital']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    
    line = FORMAT_LINE.format(territory=territory, url_territory=url_territory, capital=capital, url_capital=url_capital, url_flag=url_flag,flag_width=flag_width, flag_height=flag_height, lat=lat, lon=lon)
    wdata += line
#

with open('british_overseas_territories_coordinates.csv', 'w') as f2:
    f2.write(wdata)

