# parse_html.py
# 2013-06-01 K.OHWADA

from bs4 import BeautifulSoup

import re

BASE_URL = "https://en.wikipedia.org"
  
HTTPS = "https:"

COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

EMPTY = ''

def parse_a(data):
    if not data:
        return ["", ""]
    a = data.find("a")
    if not a:
        return ["", ""]
    a_name = a.string
    name = a_name.replace(COMMA, COMMA_HTML)
    href = a.get("href")
    url = BASE_URL +  href.replace(COMMA, COMMA_URL)
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

FORMAT_LINE = "{territory}, {url_territory}, {capital}, {url_capital}, {url_flag}, {flag_width}, {flag_height}, \n"

wdata = ""

with open('british_territories.json') as f1:
    dic = json.load(f1)

list_teritories = dic['teritories']
    
for item in list_teritories:
    teritory = item['teritory']
    url_teritory = item['url_teritory']
    capital = item['capital']
    url_capital = item['url_capital']
    url_flag = item['url_flag']
    flag_width = item['flag_width']
    flag_height = item['flag_height']

    line = FORMAT_LINE.format( territory=territory, url_territory=url_territory, capital=capital, url_capital=url_capital, url_flag=url_flag, flag_width=flag_width, flag_height=flag_height)
    wdata += line

with open('british_territories.csv', 'w') as f2:
     f2.write(wdata)
