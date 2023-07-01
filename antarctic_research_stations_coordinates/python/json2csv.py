# json2csvpy
# 2023-06-01 K.OHWADA

import json

HYPHON = '-'

FORMAT_LINE = '{station}, {url_station}, {url_station_flag}, {station_width}, {station_height}, {location}, {url_location}, {country}, {url_country_flag}, {country_width}, {country_height}, {lat}, {lon} \n'

with open('antarctic_research_stations.json') as f1:
    dic1 = json.load(f1)
    list_stations = dic1['stations']

wdata = ''

url_station_flag = HYPHON
station_width = 0
station_height = 0
lat = 0
lon =0

for item in   list_stations:
    station = item['station']
    print(station)
    url_station = item['url_station']
    location = item['location']
    url_location = item['url_location']
    country = item['country']
    url_country_flag = item['url_country_flag']
    country_width = item['country_width']
    country_height = item['country_height']

    line = FORMAT_LINE.format( station=station, url_station=url_station, url_station_flag=url_station_flag, station_width=station_width,station_height=station_height, location=location, url_location=url_location, country=country, url_country_flag=url_country_flag, country_width=country_width, country_height=country_height, lat=lat, lon=lon )
    print(line)
    wdata += line;

with open('antarctic_research_stations_coordinates.csv', 'w') as f5:
     f5.write(wdata)


