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

FORMAT_LINE = "{country}, {url_country}, {date}, {region}, {url_region}, {subregion},  {url_subregion}, {population}, {government}, {notes} \n"

wdata = ""

with open('Member_states_of_the_Commonwealth_of_Nations_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')

rows = soup.select("table tr")

for row in rows:
    th_cols = row.find_all("th")
    td_cols = row.find_all("td")
    len_th_cols = len(th_cols)
    len_td_cols = len(td_cols)
    country = ""
    url_country = "" 
    if len_th_cols >= 1:
        country, url_country = parse_a(th_cols[0])
        print(country)
    date = ""
    if len_td_cols >= 1:
        date =  strip_ref(td_cols[0])
    region = ""
    url_region = ""
    if len_td_cols >= 2:
        region, url_region = parse_a(td_cols[1])
    subregion = ""
    url_subregion = ""
    if len_td_cols >= 3:
        subregion, url_subregion = parse_a(td_cols[2])
    population = ""
    if len_td_cols >= 4:
        population =  parse_text(td_cols[3])
    government	 = ""
    if len_td_cols >= 5:
        government = strip_ref(td_cols[4])
    notes = ""
    if len_td_cols >= 6:
        notes =  strip_ref(td_cols[5])
   
    line = FORMAT_LINE.format(country=country, url_country=url_country,  date= date, region=region, url_region=url_region, subregion=subregion, url_subregion=url_subregion, population=population, government=government, notes=notes)

    print(line)
    wdata += line;

with open('commonwealth_nations.csv', 'w') as f2:
     f2.write(wdata)

