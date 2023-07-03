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

FORMAT_LINE = '{country}, {url_country}, {url_flag}, {width}, {height}, {date_dominion}, {date_adoption}, {date_final}, {final_event}, {url_final_event}, {notes} \n'

wdata = ""

with open('List_of_countries_that_have_gained_independence_from_the United_Kingdom_dominion_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
rows = soup.select('table tr')

for row in rows:
    cols = row.find_all('td')
    len_cols = len(cols)
    if len_cols < 6:
        continue
    country = ''
    url_country= ''
    url_flag = ''
    width = 0
    height = 0
    if len_cols >= 1:
        country, url_country = parse_a(cols[0])
        url_flag, width, height = parse_img(cols[0])
        print(country)
    date_dominion = ''
    if len_cols >= 2:
        date_dominion =  strip_ref(cols[1])
    date_adoption = ''
    if len_cols >= 3:
        date_adoption =  strip_ref(cols[2])
    date_final = ''
    if len_cols >= 4:
        date_final =  parse_text(cols[3])
    final_event = ''
    url_final_event = ''
    if len_cols >= 5:
        final_event,  url_final_event =  parse_a(cols[4])
    notes = ''
    if len_cols >= 6:
        notes =  parse_text(cols[5])


    line = FORMAT_LINE.format(country=country, url_country=url_country,         url_flag=url_flag, width=width, height=height, date_dominion=date_dominion, date_adoption=date_adoption, date_final=date_final, final_event=final_event, url_final_event=url_final_event, notes=notes)
    print(line)
    wdata += line;

with open('countries_from_uk_dominion.csv', 'w') as f2:
     f2.write(wdata)

