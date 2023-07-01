# json2kml.py
# 2023-06-01 K.OHWADA

import json

import urllib.parse

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_DESCRIPTION = '<![CDATA[<a href="{url_country}">{country}</a>]]>'

TEMPLATE_STYLE_URL = '#{id}'

TITLE = 'Research stations in Antarctica'

DESC = 'display the National Flag at the Coordinates of Research station'

SPACE = ' '

UNDERBAR = '_'

ALTITUDE = 0

with open('template_kml.txt', 'r') as f1:
    template_kml = f1.read()

with open('template_placemark.txt', 'r') as f2:
    template_placemark = f2.read()

with open('template_style.txt', 'r') as f3:
    template_style = f3.read()

stations =[]

placemarks = ""

styles = ""

with open('antarctic_research_stations_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    list_stations = dic['stations']
    
    for item in list_stations:
        station = item['station']
        url_station = item['url_station']
        lat = item['lat']
        lon = item['lon']
        url_country_flag = item['url_country_flag']
        print(station)
        desc = TEMPLATE_DESCRIPTION.format(url_country=url_station, country=station)
        id_station = urllib.parse.quote( station.lower().replace(SPACE, UNDERBAR) )
        style_url = TEMPLATE_STYLE_URL.format(id=id_station)
        placemark = template_placemark.format(name=station, description=desc,  lat=lat,  lon=lon, altitude=ALTITUDE,  style_url =  style_url)
        print( placemark)
        style = template_style.format(id=id_station, href=url_country_flag)

        placemarks += placemark
        styles += style

wdata = template_kml.format(name=TITLE, description=DESC, placemarks= placemarks, styles=styles)
  
with open('antarctic_research_stations.kml', 'w') as f4:
    f4.write(wdata)

