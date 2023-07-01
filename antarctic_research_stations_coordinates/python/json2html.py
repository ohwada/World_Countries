# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

TEMPLATE_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

TEMPLATE_LATLON = '({lat:.1f}, {lon:.1f})'

WIDTH = 50

ZOOM = 8


def make_coordinates(lat, lon):
    gmap = TEMPLATE_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =TEMPLATE_LATLON.format( lat=lat, lon=lon )
    atag =TEMPLATE_A_TAG.format(href=gmap, name=latlon)
    return atag
#


def make_img(url_flag, width, height):
    if width == 0:
        return ''
    h = int( (WIDTH * height) / width )
    flag = TEMPLATE_IMG.format(src=url_flag, width=WIDTH, height=h)
    return flag
#


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

stations =[]

rows=""

with open('antarctic_research_stations_coordinates.json') as f3:
    dic = json.load(f3)
    str_title = dic['title']
    desc = dic['desc']
    ref = dic['reference']
    url_ref = dic['url_reference']
    list_stations = dic['stations']
    print(str_title)
  #
 
for item in list_stations:
    station = item['station']
    url_station = item['url_station']
    url_station_flag = item['url_station_flag']
    station_width = item['station_width']
    station_height = item['station_height']
    location = item['location']
    url_location = item['url_location']
    country = item['country']
    url_country_flag = item['url_country_flag']
    country_width = item['country_width']
    country_height = item['country_height']
    lat = item['lat']
    lon = item['lon']

    row_station = TEMPLATE_A_TAG.format(href=url_station, name=station)
    row_location = TEMPLATE_A_TAG.format(href=url_location, name=location)
    row_country_flag = TEMPLATE_IMG.format(src=url_country_flag, width=country_width, height=country_height)
    row_station_flag = make_img(url_station_flag, station_width, station_height)
    row_coordinates = make_coordinates(lat, lon)

    row = template_row.format( station=row_station, location=row_location, country=country, station_flag=row_station_flag, country_flag=row_country_flag, coordinates= row_coordinates)
    print(row)
    rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('antarctic_research_stations_coordinates.html', 'w') as f4:
    f4.write(wdata)

