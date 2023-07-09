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
        return ['', '']
    a = data.find('a')
    if not a:
        return ['', '']
    a_name = a.text
    if not a_name:
        return ['', '']
    name = a_name.replace(COMMA, COMMA_HTML)
    href = a.get('href')
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

FORMAT_LINE = '{territory}, {url_territory}, {url_flag}, {flag_width}, {flag_height}, {url_arms}, {arms_width}, {arms_height},  {location}, {url_location}, {motto}, {area}, {population},  {capital}, {url_capital}, {gdp}, {gdp_per_capita}, {notes} \n'

wdata = ""

with open('British_Overseas_Territories_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')

rows = soup.select("table tr")

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    if len_cols < 11:
        continue
    url_flag = ''
    flag_width = 0, 
    flag_height = 0
    if len_cols >= 1:
        url_flag, flag_width, flag_height = parse_img(cols[0])
    url_arms = ''
    arms_width = 0, 
    arms_height = 0
    if len_cols >= 2:
        url_arms, arms_width, arms_height = parse_img(cols[1])
    territroy = ''
    url_territroy = ''
    if len_cols >= 3:
        territory, url_territory = parse_a(cols[2])
    location = ''
    url_location = ''
    if len_cols >= 4:
        location, url_location = parse_a(cols[3])
    motto = ''
    if len_cols >= 5:
        motto = parse_text(cols[4])
    area = ''
    if len_cols >= 6:
        area = strip_ref(cols[5])
    population	 = ''
    if len_cols >= 7:
        population	 = strip_ref(cols[6])
    capital = ''
    url_capital = ''
    if len_cols >= 8:
          capital, url_capital = parse_a(cols[7])
    gdp = ''
    if len_cols >= 9:
        gdp = parse_text(cols[8])
    gdp_per_capita = ''
    if len_cols >= 10:
        _per_capita = parse_text(cols[9])
    notes = ''
    if len_cols >= 11:
        notes = parse_text(cols[10])

    line = FORMAT_LINE.format(url_flag=url_flag, flag_width=flag_width, flag_height=flag_height, url_arms=url_arms, arms_width=arms_width, arms_height=arms_height, territory=territory, url_territory=url_territory, location=location, url_location=url_location, motto=motto, area=area, population=population, capital=capital, url_capital=url_capital, gdp=gdp, gdp_per_capita=gdp_per_capita, notes=notes)
    wdata += line;

with open('british_overseas_territories.csv', 'w') as f2:
     f2.write(wdata)

