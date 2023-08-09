# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse


FILE_HTML = 'tokyo_23_wards_table.html'

FILE_CSV = 'tokyo_23_wards.csv'

URL_BASE = 'https://en.wikipedia.org'

HTTPS = 'https:'

FORMAT_LINE = '{name_ward}, {url_ward}, {url_flag}, {flag_width}, {flag_height}, {url_emblem}, {emblem_width}, {emblem_height}, {population}, {area}, {density} \n'


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
    if len_cols < 6:
        continue
    name_ward = EMPTY
    url_ward = EMPTY
    if len_cols >= 1:
        name_ward, url_ward = parse_a(cols[0])
        print(name_ward)
    url_flag = EMPTY
    flag_width = 0
    flag_height = 0
    if len_cols >= 2:
        url_flag, flag_width, flag_height = parse_img(cols[1])
    url_emblem = EMPTY
    emblem_width = 0
    emblem_height = 0
    if len_cols >= 3:
        url_emblem,  emblem_width,  emblem_height = parse_img(cols[2])
    population = EMPTY
    if len_cols >= 4:
         population = parse_text(cols[3])
    area = EMPTY
    if len_cols >= 5:
         area = parse_text(cols[4])
    density = EMPTY
    if len_cols >= 6:
         density = parse_text(cols[5])
    line = FORMAT_LINE.format(name_ward=name_ward, url_ward=url_ward, url_flag=url_flag, flag_width=flag_width,  flag_height= flag_height, url_emblem=url_emblem, emblem_width=emblem_width, emblem_height= emblem_height, population=population, area=area, density=density)
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

