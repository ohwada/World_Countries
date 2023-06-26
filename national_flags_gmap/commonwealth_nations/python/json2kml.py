# json2kml.py
# 2023-06-01 K.OHWADA

import json

import urllib.parse

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_DESCRIPTION = '<![CDATA[<a href="{url_country}">{country}</a>]]>'

TEMPLATE_STYLE_URL = '#{id}'

TITLE = 'Commonwealth Nations'

DESC = 'display the National Flag at the Coordinates of the Capital'

SPACE = ' '

UNDERBAR = '_'

ALTITUDE = 0

with open('template_kml.txt', 'r') as f1:
    template_kml = f1.read()

with open('template_placemark.txt', 'r') as f2:
    template_placemark = f2.read()

with open('template_style.txt', 'r') as f3:
    template_style = f3.read()

countries =[]

placemarks = ""

styles = ""

with open('commonwealth_nations_capital.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    list_countries = dic['countries']
    
    for item in list_countries:
        country = item['country']
        url_country = item['url_country']
        capital = item['capital']
        url_capital = item['url_capital']
        lat = item['lat']
        lon = item['lon']
        url_flag_icon = item['url_flag_icon']
        print(country)
        desc = TEMPLATE_DESCRIPTION.format(url_country=url_country, country=country)
        id_country = urllib.parse.quote( country.lower().replace(SPACE, UNDERBAR) )
        style_url = TEMPLATE_STYLE_URL.format(id=id_country)
        placemark = template_placemark.format(name=country, description=desc,  lat=lat,  lon=lon, altitude=ALTITUDE,  style_url =  style_url)
        print( placemark)
        style = template_style.format(id=id_country, href=url_flag_icon)

        placemarks += placemark
        styles += style

wdata = template_kml.format(name=TITLE, description=DESC, placemarks= placemarks, styles=styles)
  
with open('ommonwealth_nations_capital..kml', 'w') as f4:
    f4.write(wdata)

