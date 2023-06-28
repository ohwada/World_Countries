# json2kml.py
# 2023-06-01 K.OHWADA

import json

import urllib.parse

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_DESCRIPTION = '<![CDATA[<a href="{url_country}">{country}</a>]]>'

TEMPLATE_STYLE_URL = '#{id}'

TITLE = 'Crown Dependencies'

DESC = 'display the Flag at the Coordinates of Islands'

SPACE = ' '

UNDERBAR = '_'

ALTITUDE = 0

with open('template_kml.txt', 'r') as f1:
    template_kml = f1.read()

with open('template_placemark.txt', 'r') as f2:
    template_placemark = f2.read()

with open('template_style.txt', 'r') as f3:
    template_style = f3.read()

teritories =[]

placemarks = ""

styles = ""

with open('crown_dependencies_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    list_teritories = dic['teritories']
    
    for item in list_teritories:
        island = item['island']
        url_island = item['url_island']
        lat = item['lat']
        lon = item['lon']
        url_flag = item['url_flag']
        print(island)
        desc = TEMPLATE_DESCRIPTION.format(url_country=url_island, country=island)
        id_island = urllib.parse.quote( island.lower().replace(SPACE, UNDERBAR) )
        style_url = TEMPLATE_STYLE_URL.format(id=id_island)
        placemark = template_placemark.format(name=island, description=desc,  lat=lat,  lon=lon, altitude=ALTITUDE,  style_url =  style_url)
        print( placemark)
        style = template_style.format(id=id_island, href=url_flag)

        placemarks += placemark
        styles += style

wdata = template_kml.format(name=TITLE, description=DESC, placemarks= placemarks, styles=styles)
  
with open('crown_dependencies.kml', 'w') as f4:
    f4.write(wdata)

