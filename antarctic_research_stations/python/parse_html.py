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

FORMAT_LINE = '{station}, {url_station}, {location}, {url_location}, {country}, {url_country_flag}, {flag_width}, {flag_height}, {admin}, {url_admin}, {year}, {max_pers}, {summer},  {winter}, {locode}, {offset}, {url_offset}, {temp}  \n'

wdata = ""

with open('Research_stations_in_Antarctica _table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
rows = soup.select("table tr")

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    if len_cols < 10:
        continue
    station = ''
    url_station =  ''
    if len_cols >= 1:
        station, url_station = parse_a(cols[0])
    location = ''
    url_location =  ''
    if len_cols >= 2:
        location, url_location = parse_a(cols[1])
    country=  ''
    url_country_flag = ''
    flag_width = 0
    flag_height = 0
    if len_cols >= 3:
        country = parse_text(cols[2])
        url_country_flag, flag_width, flag_height = parse_img(cols[2])
    admin = ''
    url_admin =  ''
    if len_cols >= 4:
        admin, url_admin = parse_a(cols[3])
    year =  ''
    if len_cols >= 5:
        year = parse_text(cols[4])
    max_pers =  ''
    if len_cols >= 6:
        max_pers = parse_text(cols[5])
    summer =  ''
    if len_cols >= 7:
        summer = parse_text(cols[6])
    winter =  ''
    if len_cols >= 8:
        winter = parse_text(cols[7])
    locode	 =  ''
    if len_cols >= 9:
         locode  = parse_text(cols[8])
    offset	 =  ''
    url_offset = ''
    if len_cols >= 10:
         offset, url_offset  = parse_a(cols[9])
    temp	 =  ''
    if len_cols >= 11:
         temp  = parse_text(cols[10])

    line = FORMAT_LINE.format( station=station, url_station=url_station, location=location, url_location=url_location, country=country, admin=admin, url_admin=url_admin, url_country_flag= url_country_flag, flag_width=flag_width, flag_height=flag_height, year=year, max_pers=max_pers, summer=summer, winter=winter, locode=locode, offset=offset,  url_offset=url_offset, temp=temp )

    print(line)
    wdata += line;

with open('antarctic_research_stations.csv', 'w') as f2:
     f2.write(wdata)

