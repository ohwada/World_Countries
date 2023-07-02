# parse_html.py
# 2013-06-01 K.OHWADA

from bs4 import BeautifulSoup

import re

BASE_URL = "https://en.wikipedia.org"
  
HTTPS = "https:"

COMMA = ','

COMMA_HTML = '&comma;'

EMPTY = ''

def parse_a(data):
    if not data:
        return ["", ""]
    a = data.find("a")
    if not a:
        return ["", ""]
    name = a.string
    href = a.get("href")
    url = BASE_URL + href
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

FORMAT_LINE = "{country}, {url_country}, {pre_name}, {date}, {year}, {notes}\n"

wdata = ""

with open('List_of_countries_that_have_gained_independence_ from_the_United_Kingdom _table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
#table = soup.find_all("table")
# print(table)

rows = soup.select("table tr")
#print(tr)

for row in rows:
    # print(row)
    cols = row.find_all("td")
    # print(cols)
    len_cols = len(cols)
    name = ""
    url= "" 
    if len_cols >= 1:
        # print(th_cols[0])
        name, url = parse_a(cols[0])
        print(name)
    pre_name= ""
    if len_cols >= 2:
        pre_name =  strip_ref(cols[1])
    date= ""
    if len_cols >= 3:
        date =  parse_text(cols[2])
    year= ""
    if len_cols >= 4:
        year =  parse_text(cols[3])
    notes= ""
    if len_cols >= 5:
        notes =  strip_ref(cols[4])

    line = FORMAT_LINE.format(country=name, url_country=url, pre_name=pre_name, date=date, year=year, notes=notes)
    print(line)
    wdata += line;

with open('countries_from_uk.csv', 'w') as f2:
     f2.write(wdata)

