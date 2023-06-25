# parse_html.py
# 2023-06-01 K.OHWADA

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

def parse_date(data):
    if not data:
        return ""
    span = data.find("span")
    if not span:
        return ""
    date = span.string
    return date
#

def parse_orig(data):
    if not data:
        return ""
    img = data.find("img")
    if not img:
        return ""
    title = img.get("title")
    return title
#

FORMAT_LINE = "{country}, {url_country}, {population}, {year}, {governor}, {url_overnor}, {prime_minister}, {url_prime_minister} \n"

wdata = ""

with open('Commonwealth realm _table.html', 'r') as f1:
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
    country = ""
    url_country = "" 
    if len_cols >= 1:
        country, url_country = parse_a(cols[0])
        print(country)
    population = ""
    if len_cols >= 2:
        population =  parse_text(cols[1])
    year= ""
    if len_cols >= 3:
        year = parse_text(cols[2])

    governor= ""
    url_governor= ""
    if len_cols >= 4:
        governor, url_governor = parse_a(cols[3])
    prime_minister= ""
    url_prime_minister= ""
    if len_cols >= 5:
        prime_minister, url_prime_minister = parse_a(cols[4])

    line = FORMAT_LINE.format(country=country, url_country=url_country,  population=population, year=year, governor=governor, url_overnor=url_governor, prime_minister=prime_minister, url_prime_minister=url_prime_minister)
    print(line)
    wdata += line;

with open('commonwealth_realm .csv', 'w') as f2:
     f2.write(wdata)

