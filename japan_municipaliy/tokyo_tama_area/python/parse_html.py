# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse


FILE_HTML = 'tama_area_table.html'

FILE_CSV = 'tama_area.csv'

URL_BASE = 'https://jp.wikipedia.org'

HTTPS = 'https:'

FORMAT_LINE = '{number}, {code}, {name_city}, {url_city}, {url_flag}, {flag_width}, {flag_height}, {population}, {area}, {density}, {revenue}, {established} \n'


COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

LF = '\n'

LF_HTML = '&#010;'

EMPTY = ''

SPACE = ' '

HYPHEN = '-'


def parse_b_a(data):
    if not data:
        return ['', '']
    b = data.find('b')
    if not b:
        return ['', '']
    a = b.find('a')
    if not a:
        return ['', '']
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

rows = soup.select("table tr")

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    if len_cols < 8:
        continue
    number = EMPTY
    if len_cols >= 1:
        number = parse_text(cols[0])
    code = EMPTY
    if len_cols >= 2:
        code = parse_text(cols[1])
    name_city = EMPTY
    url_city = EMPTY
    url_flag = EMPTY
    flag_width = 0
    flag_height = 0
    if len_cols >= 3:
        name_city, url_city = parse_b_a(cols[2])
        print(name_city)
        url_flag, flag_width, flag_height = parse_img(cols[2])
    population = EMPTY
    if len_cols >= 4:
         population = parse_text(cols[3])
    area = EMPTY
    if len_cols >= 5:
         area = parse_text(cols[4])
    density = EMPTY
    if len_cols >= 6:
         density = parse_text(cols[5])
    revenue = EMPTY
    if len_cols >= 7:
        revenue = parse_text(cols[6])
    established = EMPTY
    if len_cols >= 8:
        established = parse_text(cols[7])
    line = FORMAT_LINE.format(number=number, code=code, name_city=name_city, url_city=url_city, url_flag=url_flag, flag_width=flag_width,  flag_height= flag_height, population=population, area=area, density=density, revenue=revenue, established=established )
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

