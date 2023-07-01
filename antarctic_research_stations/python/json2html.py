# json2html.py
# 2023-06-01 K.OHWADA

import json

TEMPLATE_A_TAG = '<a href="{href}">{name}</a>'

TEMPLATE_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

stations =[]

rows=""

with open('antarctic_research_stations.json') as f3:
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
    location = item['location']
    url_location = item['url_location']
    country = item['country']
    url_country_flag = item['url_country_flag']
    country_width = item['country_width']
    country_height = item['country_height']
    admin = item['admin']
    url_admin = item['url_admin']
    yearest = item['yearest']
    max_pers = item['max_pers']
    summer_pop = item['summer_pop']
    winter_pop = item['winter_pop']
    locode = item['locode']
    utc_offset = item['utc_offset']
    url_utc_offset = item['url_utc_offset']
    mean_annual_temp = item['mean_annual_temp']

    row_station = TEMPLATE_A_TAG.format(href=url_station, name=station)
    row_location = TEMPLATE_A_TAG.format(href=url_location, name=location)
    row_admin = TEMPLATE_A_TAG.format(href=url_admin, name=admin)
    row_utc_offset = TEMPLATE_A_TAG.format(href=url_utc_offset, name=utc_offset)
    row_country_flag = TEMPLATE_IMG.format(src=url_country_flag, width=country_width, height=country_height)

    row = template_row.format( station=row_station, location=row_location, country=country, country_flag=row_country_flag, admin=row_admin, yearest=yearest, max_pers=max_pers, summer_pop=summer_pop, winter_pop=winter_pop, locode=locode, utc_offset=row_utc_offset,mean_annual_temp=mean_annual_temp )
    print(row)
    rows +=  row
#

html_ref = TEMPLATE_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc = desc, reference=html_ref, rows=rows)
  
with open('antarctic_research_stations.html', 'w') as f4:
    f4.write(wdata)

