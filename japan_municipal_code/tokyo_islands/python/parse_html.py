# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse


FILE_HTML = 'tokyo_islands_table.html'

FILE_CSV = 'tokyo_islands.csv'

URL_BASE = 'https://ja.wikipedia.org'

HTTPS = 'https:'

FORMAT_LINE = '{number}, {url_flag}, {flag_width}, {flag_height}, {name_municipality}, {url_municipality}, {name_location}, {url_location}  \n'


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
    if len_cols < 4:
        continue
    number = EMPTY
    if len_cols >= 1:
        number = parse_text(cols[0])
    url_flag = EMPTY
    flag_width = 0
    flag_height = 0
    if len_cols >= 2:
        url_flag, flag_width, flag_height = parse_img(cols[1])
    name_municipality = EMPTY
    url_municipality = EMPTY
    if len_cols >= 3:
        name_municipality, url_municipality = parse_a(cols[2])
    name_location = EMPTY
    url_location = EMPTY
    if len_cols >= 4:
        name_location, url_location = parse_a(cols[3])
    line = FORMAT_LINE.format( number=number, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height, name_municipality=name_municipality, url_municipality=url_municipality, name_location=name_location, url_location=url_location)
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

