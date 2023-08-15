# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse


FILE_HTML = 'japan_designated_city_list_wikipedia_table.html'


FILE_CSV = 'japan_designated_city_list_wikipedia.csv'


FILE_WARDS = 'wards.csv'


FORMAT_LINE = '{name_region}, {url_region}, {name_pref}, {url_pref}, {name_city}, {url_city}, {url_emblem}, {emblem_width}, {emblem_height}, {url_flag}, {flag_width}, {flag_height}, {estimated_population}, {did_population}, {area}, {urban_area}, {density}, {did_density}, {financial_index}, {number_of_companies}, {date} \n'

FORMAT_WARD = '{city}, {name}, {url} \n'


URL_BASE = 'https://ja.wikipedia.org'

HTTPS = 'https:'


COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

EMPTY = ''


def parse_a(data):
    if not data:
        return ['', '']
    a = data.find('a')
    if not a:
        str_name = data.text.strip()
        return[str_name, '']
    a_name = a.text
    if not a_name:
        return ['', '']
    name = a_name.replace(COMMA, COMMA_HTML)
    href = a.get('href')
    path = href.replace(COMMA, COMMA_URL)
    url = urllib.parse.urljoin(URL_BASE, path)
    return [name, url]
#


def parse_img(data):
    if not data:
        return ["", 0, 0]
    img = data.find("img")
    if not img:
        return ["", 0, 0]
    src = img.get("src")
    width = img.get("width")
    height = img.get("height")
    return [src, width, height]
#


def parse_text(data):
    if not data:
        return ''
    str1 = data.text.strip()
    ret = str1.replace(COMMA, COMMA_HTML)
    return ret
#


def parse_wards(name_city, data):
    wards = ''
    if not data:
        return ''
    arr = data.find_all('li')
    if not arr:
        return ''
    for item in arr:
        name, url = parse_a(item)
        ward = FORMAT_WARD.format(city=name_city, name=name, url=url)
        wards += ward
    return wards
#


lines = ''

wdata = ''


with open(FILE_HTML, 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')

rows = soup.select('table tr')

prev_name_region = ''
prev_url_region = ''
prev_name_pref = ''
prev_url_pref = ''


for row in rows:
    cols = row.find_all('td')
    len_cols = len(cols)
    print('len: ', len_cols)
    if len_cols < 13:
        continue

    name_region = prev_name_region
    url_region = prev_url_region
    name_pref = prev_name_pref
    url_pref = prev_url_pref
    base = 0

    if len_cols == 15:
        name_region, url_region = parse_a(cols[0])
        name_pref, url_pref = parse_a(cols[1])
        base = 2
    elif len_cols == 14:
        name_pref, url_pref = parse_a(cols[0])
        base = 1

    if name_pref == name_region:
        url_pref = url_region

    name_city, url_city = parse_a(cols[base + 0])
    url_emblem, emblem_width, emblem_height = parse_img( cols[ base +1] )
    url_flag, flag_width, flag_height = parse_img(cols[base + 2] )
    estimated_population = parse_text(cols[base +3])
    did_population = parse_text(cols[base + 4])
    area = parse_text(cols[base + 5])
    urban_area = parse_text(cols[base + 6])
    density = parse_text(cols[base + 7])
    did_density = parse_text(cols[base + 8] )
    financial_index = parse_text(cols[ base + 9] )
    number_of_companies = parse_text (cols[base + 10] )
    date = parse_text( cols[base + 11] )
    wards = cols[base + 12]
    wdata += parse_wards(name_city, wards)

    prev_name_region = name_region
    prev_url_region = url_region
    prev_name_pref = name_pref
    prev_url_pref = url_pref

    line = FORMAT_LINE.format( name_region=name_region, url_region= url_region, name_pref=name_pref, url_pref=url_pref, name_city=name_city, url_city=url_city, url_emblem=url_emblem, emblem_width=emblem_width, emblem_height=emblem_height, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height, estimated_population=estimated_population, did_population=did_population, area=area, urban_area=urban_area, density=density, did_density=did_density, financial_index=financial_index, number_of_companies=number_of_companies, date=date)
    print(line)
    lines += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(lines)
#


with open(FILE_WARDS, 'wt') as f3:
     f3.write(wdata)
#