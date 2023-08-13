# json2html.py
# 2023-06-01 K.OHWADA

import json


FILE_JSON = 'japan_prefecture_detail_list.json'

FILE_HTML = 'japan_prefecture_detail_list.html'


FORMAT_A_TAG = '<a href="{href}" target="_blank">{name}</a>'

FORMAT_IMG = '<img src="{src}" decoding="async"  width="{width}" height="{height}" />'

FORMAT_GMAP ='https://www.google.com/maps/@{lat},{lon},{zoom}z'

FORMAT_LATLON = '({lat:.1f}, {lon:.1f})'


ZOOM = 12


def make_link(name, url):
    if not url:
        return name
    atag = FORMAT_A_TAG.format(href=url, name=name)
    return atag
#



def make_coordinates(lat, lon):
    gmap = FORMAT_GMAP.format(lat=lat, lon=lon, zoom=ZOOM)
    latlon =FORMAT_LATLON.format( lat=lat, lon=lon )
    atag =FORMAT_A_TAG.format(href=gmap, name=latlon)
    return atag
#


with open('files/template_html.txt', 'r') as f1:
    template_html = f1.read()
#

with open('files/template_row.txt', 'r') as f2:
    template_row = f2.read()
#

rows = ''

with open(FILE_JSON, 'r') as f3:
    dic = json.load(f3)
#

title_ja = dic['title_ja']
ref = dic['reference']
url_ref = dic['url_reference']
list_prefectures = dic['prefectures']


for item in list_prefectures :
    code = item['code']
    name_pref = item['name_pref']
    url_pref = item['url_pref']
    yomi = item['yomi']
    name_capital = item['name_capital_city']
    url_capital = item['url_capital_city']
    name_largest = item['name_largest_city']
    url_largest = item['url_largest_city']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']
    region = item['region']
    population = item['population']
    area = item['area']
    density = item['population_density']
    number_of_cities = item['number_of_cities']
    diet_member_quota = item['diet_member_quota']

    row_pref = FORMAT_A_TAG.format(href=url_pref, name=name_pref)
    row_capital = FORMAT_A_TAG.format(href=url_capital, name=name_capital)
    row_largest = make_link(name_largest, url_largest)
    row_flag = FORMAT_IMG.format(src=url_flag, width=flag_width, height=flag_height)
    row = template_row.format(code=code,  pref=row_pref, yomi=yomi, capital=row_capital, largest=row_largest, flag=row_flag, region=region, population=population, area =area, density=density, number_of_cities=number_of_cities, diet=diet_member_quota )
    print(row)
    rows +=  row
#


html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=title_ja, reference=html_ref, rows=rows)


with open(FILE_HTML, 'wt') as f4:
    f4.write(wdata)
#

