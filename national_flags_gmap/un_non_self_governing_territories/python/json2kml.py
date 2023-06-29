# json2kml.py
# 2023-06-01 K.OHWADA

import json

import urllib.parse

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_DESCRIPTION = '<![CDATA[<a href="{url_country}">{country}</a>]]>'

TEMPLATE_STYLE_URL = '#{id}'

TITLE = 'United Nations List of non-self-governing Territories'

DESC = 'display the Flag at the Coordinates of Territories'

SPACE = ' '

UNDERBAR = '_'

ALTITUDE = 0

with open('template_kml.txt', 'r') as f1:
    template_kml = f1.read()

with open('template_placemark.txt', 'r') as f2:
    template_placemark = f2.read()

with open('template_style.txt', 'r') as f3:
    template_style = f3.read()


placemarks = ""

styles = ""


with open('un_non_self_governing_territories_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    list_teritories = dic['teritories']
    
    for item in     list_teritories:
        teritory = item['teritory']
        url_teritory = item['url_teritory']
        url_teritory_flag = item['url_teritory_flag']
        teritory_width = item['teritory_width']
        teritory_height = item['teritory_height']
        lat = item['lat']
        lon = item['lon']
        print()
        desc = TEMPLATE_DESCRIPTION.format(url_country=url_teritory, country=teritory)
        id_teritory = urllib.parse.quote( teritory.lower().replace(SPACE, UNDERBAR) )
        style_url = TEMPLATE_STYLE_URL.format(id=id_teritory)
        placemark = template_placemark.format(name=teritory, description=desc,  lat=lat,  lon=lon, altitude=ALTITUDE,  style_url =  style_url)
        print( placemark)
        style = template_style.format(id=id_teritory, href=url_teritory_flag)

        placemarks += placemark
        styles += style

wdata = template_kml.format(name=TITLE, description=DESC, placemarks= placemarks, styles=styles)
  
with open('un_non_self_governing_territories_coordinates.kml', 'w') as f4:
    f4.write(wdata)

