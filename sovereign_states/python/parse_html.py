# parse_html.py
# 2023-06-01 K.OHWADA

from bs4 import BeautifulSoup

import re

BASE_URL = "https://en.wikipedia.org"
  
HTTPS = "https:"

FORMAT_LINE = "{country}, {formal_name}, {url_country}, {url_flag}, {width}, {height}, {membership}, {dispute}, {info} \n"

COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

NAME_SEPARATER = '–'

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

def parse_formal_name(data):
    if not data:
        return ""
    str_data = data.text.strip()
    arr = str_data.split(NAME_SEPARATER)
    len_arr = len(arr)
    ret = ""
    if len_arr >=2:
        ret = arr[1].strip()
    return ret
#

def strip_a(data):
    if not data:
        return ""
    str_data = data.text.strip()
    ret = str_data.replace('A ', '')
    return ret
#

wdata = ""

with open('List_of_sovereign_states _table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')

rows = soup.select("table tr")

for row in rows:
    print(row)
    cols = row.find_all("td")
    print(cols)
    len_cols = len(cols)
    print("len", len_cols)
    country = ""
    url_coubtry= "" 
    url_flag = ""
    width = 0
    height = 0
    formal_name = ""
    if len_cols >= 1:
        country, url_country = parse_a(cols[0])
        url_flag, width, height = parse_img(cols[0])
        formal_name = parse_formal_name(cols[0])
        print(country)
    membership = ""
    if len_cols >= 2:
        membership = strip_a(cols[1])
    dispute = ""
    if len_cols >= 3:
        dispute = strip_a(cols[2])
    info = ""
    if len_cols >= 4:
        info = parse_text(cols[3])
       
    line = FORMAT_LINE.format(country=country, url_country=url_country, formal_name=formal_name, url_flag=url_flag, width =width, height= height, membership = membership, dispute= dispute,  info=info)
    print(line)
    wdata += line;

with open('sovereign_states.csv', 'w') as f2:
     f2.write(wdata)

