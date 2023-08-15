# json2html.py
# 2023-06-01 K.OHWADA

import json

FILE_JSON = 'japan_designated_city_detail_list.json'

FILE_HTML = 'japan_designated_city_detail_list.html'


FORMAT_IMG = '<img src="{src}" width="{width}" height="{height}" />'

FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_WARD = '<li><a href="{href}" target="_blank" style="font-size: 16px; line-height: 4px; ">{name}</a></li> \n'

FORMAT_WARDS = '<ul>{wards}</ul>'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'

LF_HTML = '&#010;'

BR = '<br/>'

WIDTH = 40

ZOOM = 10


def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#


def make_words(list_wards):
    wards = ''
    for item in list_wards:
        name_ward = item['name_ward'] 
        url_ward = item['url_ward']
        ward = FORMAT_WARD.format(href=url_ward, name=name_ward)
        wards +=  ward
    ret = FORMAT_WARDS.format( wards=wards)
    return ret
#



def  replace_lf(data):
    if not data:
        return ""
    ret = data.replace(LF_HTML,  BR)
    return ret
#




with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open(FILE_JSON) as f3:
    dic = json.load(f3)
#

title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
list_cities = dic['cities']


for item in list_cities :
    name_region  = item['name_region']
    url_region  = item['url_region']
    name_pref  = item['name_pref']
    url_pref  = item['url_pref']
    name_city  = item['name_city']
    url_city = item['url_city']
    url_emblem = item['url_emblem']
    emblem_width = item['emblem_width']
    emblem_height = item['emblem_height']
    url_flag = item['url_flag']
    flag_width = item[f'flag_width']
    flag_height = item[f'flag_height']
    estimated_population  = item['estimated_population']
    did_population= item['did_population']
    area  = item['area']
    urban_area  = item['urban_area']
    population_density  = item['population_density']
    did_population_density  = item['did_population_density']
    financial_index = item['financial_index']
    number_of_companies = item['number_of_companies']
    date = item['date']
    wards  = item['wards']
     
    row_region  = FORMAT_A_TAG.format(href=url_region, name=name_region)
    row_pref  = FORMAT_A_TAG.format(href=url_pref, name=name_pref)
    row_city  = FORMAT_A_TAG.format(href=url_city, name=name_city)
    row_emblem = FORMAT_IMG.format(src=url_emblem, width=emblem_width, height=emblem_height)
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row_wards = make_words(wards)

    row = template_row.format( region=row_region, pref=row_pref, 
city=row_city, emblem=row_emblem, flag=row_flag, 
estimated_population=estimated_population, did_population= did_population, area=area, urban_area=urban_area, population_density=    population_density, did_population_density=did_population_density,
financial_index=financial_index, number_of_companies=number_of_companies, date=date, wards=row_wards)
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)
  
with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

