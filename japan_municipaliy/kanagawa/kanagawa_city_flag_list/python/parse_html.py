# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup
import urllib.parse
import re


FILE_HTML = 'kanagawa_city_flag_list_table.html'

FILE_CSV = 'kanagawa_city_flag_list.csv'

URL_BASE = 'https://ja.wikipedia.org'

HTTPS = 'https:'

FORMAT_LINE = '{colspan}, {name_city}, {url_city}, {url_flag}, {flag_width}, {flag_height}, {enactment}, {date}, {color}, {notes} \n'


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


def strip_ref(data):
    if not data:
        return ""
    text1 = data.text.strip()
    text2 = text1.replace(COMMA, COMMA_HTML)
    ret = re.sub('\[\w{1,2}\]',  EMPTY, text2)
    return ret
#


def parse_colspan(data):
    if not data:
        return 0
    colspan = data.get('colspan')
    if not colspan:
        return 0
    return colspan
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
    print('len: ', len_cols)
    date = EMPTY
    if len_cols == 6:
        base = 1
        date = strip_ref(cols[3])
    elif len_cols == 5:
        base = 0
    else:
        continue
    name_city, url_city = parse_a(cols[0])
    url_flag, flag_width, flag_height = parse_img(cols[1])
    enactment = strip_ref(cols[2])
    colspan = parse_colspan(cols[2])
    color = strip_ref(cols[base+3])
    notes = strip_ref(cols[base+4])
    line = FORMAT_LINE.format(colspan=colspan, name_city=name_city, url_city=url_city, url_flag=url_flag, flag_width=flag_width,  flag_height= flag_height, enactment=enactment, date=date, color=color, notes= notes )
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

