# parse_html.py

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
        return ['', '']
    a = data.find('a')
    if not a:
        return ['', '']
    a_name = a.text
    name = a_name.replace(COMMA, COMMA_HTML)
    href = a.get('href')
    url = BASE_URL +  href.replace(COMMA, COMMA_URL)
    return [name, url]
#

def parse_img(data):
    if not data:
        return ["", 0, 0]
    img = data.find('img')
    if not img:
        return ["", 0, 0]
    src = img.get('src')
    width = img.get('width')
    height = img.get('height')
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

def parse_rowspan(data):
    if not data:
        return 0
    rowspan = data.get('rowspan')
    if not rowspan:
        return 0
    return   rowspan
#

FORMAT_LINE = " {id}, {group}, {rowspan}, {territory}, {url_territory}, {location}, {url_location}, {monarch}, {url_monarch}, {area}, {population}, {url_flag}, {flag_width}, {flag_height}, {url_arms}, {arms_width}, {arms_height}, {capital}, {url_capital}, {airport}, {url_airport} \n"

wdata = ""

with open('Crown Dependencies _table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
rows = soup.select("table tr")

id = 0

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    print('len: ', len_cols)
    if len_cols < 4:
        continue

    group = id
    id += 1
    base = 0
    rowspan = 0
    territory =  ''
    url_territory =  ''
    location =  ''
    url_location =  ''
    monarch = ''
    url_monarch = ''
    area= ''
    population =  ''
    url_flag = '' 
    flag_width = 0
    flag_height = 0
    url_arms = ''
    arms_width = 0 
    arms_height = 0
    capital = ''
    url_capital = ''
    airport = ''
    url_airport = ''

    if len_cols >= 9:
        group = 0
        base = 5
        rowspan = parse_rowspan(cols[0])
        territory, url_territory = parse_a(cols[0])
        print(territory)
        location, url_location = parse_a(cols[1])
        monarch, url_monarch = parse_a(cols[2])
        area = strip_ref(cols[3])
        population = strip_ref(cols[4])

    if len_cols >= 4:
        url_flag, flag_width, flag_height = parse_img(cols[base+0])
        url_arms, arms_width, arms_height = parse_img(cols[base+1])
        capital, url_capital = parse_a(cols[base+2])
        airport, url_airport = parse_a(cols[base+3])

    line = FORMAT_LINE.format( id=id, group=group, rowspan=rowspan, territory=territory, url_territory= url_territory, location=location, url_location= url_location, monarch=monarch, url_monarch=url_monarch, area= area, population=population, url_flag=url_flag, flag_width=flag_width,  flag_height=flag_width, url_arms=url_arms, arms_width=arms_width, arms_height=arms_height, capital=capital, url_capital=url_capital, airport=airport, url_airport=url_airport )
    print(line)
    wdata += line;

with open('crown_dependencies.csv', 'w') as f2:
     f2.write(wdata)

