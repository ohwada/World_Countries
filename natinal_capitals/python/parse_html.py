# parse_html.py
# 2023-06-01 K.OHWADA

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
 
def strip_ref(data):
    if not data:
        return ""
    text1 = data.text.strip()
    text2 = text1.replace(COMMA, COMMA_HTML)
    ret = re.sub('\[\w{1,2}\]',  EMPTY, text2)
    return ret
#

FORMAT_LINE = "{country}, {url_country}, {capital}, {url_capital}, {url_flag}, {width}, {height}, {notes}\n"

wdata = ""

with open('List of national capitals_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')

rows = soup.select("table tr")

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    print("len", len_cols)
    if len_cols == 0:
        continue
    country = ""
    url_country= "" 
    img_url = "" 
    width = 0
    height = 0
    if len_cols >= 1:
        name0, url0 = parse_a(cols[0])
        print(name0)
    name1 = ""
    url1 = "" 
    img_url = "" 
    width = 0
    height = 0
    if len_cols >= 2:
        name1, url1 = parse_a(cols[1])
        img_url, width, height = parse_img(cols[1])
        print(name1)
    notes = ""
    if len_cols >= 3:
        notes = strip_ref(cols[2])

    line = FORMAT_LINE.format(country=name1, url_country=url1, capital=name0, url_capital=url0, url_flag=img_url, width =width, height= height, notes=notes)
    print(line)
    wdata += line;

with open('captals.csv', 'w') as f2:
     f2.write(wdata)

