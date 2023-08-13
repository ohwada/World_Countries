# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse


FILE_HTML = 'japan_pref_list_table.html'

FILE_CSV = 'japan_pref_list.csv'


URL_BASE = 'https://ja.wikipedia.org'

HTTPS = 'https:'

FORMAT_LINE = '{code}, {name_pref}, {url_pref}, {yomi}, {name_capital},  {url_capital}, {name_largest_city}, {url_largest_city}, {url_flag}, {flag_width}, {flag_height}, {region}, {population}, {area}, {density}, {number_of_cities}, {diet_constant} \n'


COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

LF = '\n'

LF_HTML = '&#010;'

EMPTY = ''

SPACE = ' '

HYPHEN = '-'


def parse_a(data):
    if not data:
        return ['', '']
    a = data.find('a')
    if not a:
        str_name = data.text.strip()
        return [str_name, '']
    a_name = a.text.strip()
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
    url = HTTPS + src
    return [url, width, height]
#


def parse_text(data):
    if not data:
        return ""
    str_data = data.text.strip()
    ret = str_data.replace(COMMA, COMMA_HTML)
    return ret
#




wdata = ""


with open(FILE_HTML, 'r') as f1:
     html = f1.read()
#
 
soup = BeautifulSoup(html,'html.parser')

rows = soup.select('table tr')

for row in rows:
    cols = row.find_all('td')
    th = row.find('th')
    len_cols = len(cols)
    if len_cols < 10:
        continue
    name_pref, url_pref = parse_a(th)
    code = EMPTY
    if len_cols >= 1:
        code = parse_text(cols[0])
    yomi = EMPTY
    if len_cols >= 2:
        yomi = parse_text(cols[1])
    name_capital = EMPTY
    url_capital = EMPTY
    if len_cols >= 3:
        name_capital, url_capital = parse_a(cols[2])
    name_largest = EMPTY
    url_largest = EMPTY
    if len_cols >= 4:
        name_largest, url_largest = parse_a(cols[3])
    url_flag = EMPTY
    flag_width = 0
    flag_height = 0
    if len_cols >= 5:
        url_flag, flag_width, flag_height = parse_img(cols[4])
    region = EMPTY
    if len_cols >= 6:
        region = parse_text(cols[5])
    population = EMPTY
    if len_cols >= 7:
         population = parse_text(cols[6])
    area = EMPTY
    if len_cols >= 8:
         area = parse_text(cols[7])
    density = EMPTY
    if len_cols >= 9:
         density = parse_text(cols[8])
    number_of_cities = EMPTY
    if len_cols >= 10:
           number_of_cities = parse_text(cols[9])
    diet = EMPTY
    if len_cols >= 11:
         diet = parse_text(cols[10])

    line = FORMAT_LINE.format( code=code, name_pref=name_pref, url_pref=url_pref, yomi=yomi, name_capital=name_capital,  url_capital=url_capital, name_largest_city=name_largest, url_largest_city=url_largest, url_flag=url_flag,  flag_width=flag_width, flag_height=flag_height, region=region, population=population, area=area, density=density, number_of_cities=number_of_cities, diet_constant=diet )
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

