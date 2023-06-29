# parse_html.py

from bs4 import BeautifulSoup

import re

BASE_URL = 'https://en.wikipedia.org'
  
HTTPS = 'https:'

COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

EMPTY = ''

LF = '\n'

def parse_a_img(data):
    if not data:
        return ['', '']
    a_all = data.find_all('a')
    if not a_all:
        text = data.text
        return [text, '']
    for a in a_all:
        a_class = a.get('class')
        if a_class:
            continue
        a_text = a.text
        name = a_text.replace(COMMA, COMMA_HTML)
        href = a.get('href')
        url = BASE_URL +  href.replace(COMMA, COMMA_URL)
        return [name, url]
#


def parse_a(data):
    if not data:
        return ['', '']
    a = data.find('a')
    if not a:
        text = data.text.strip()
        return [text, '']
    a_text = a.text
    name = a_text.replace(COMMA, COMMA_HTML)
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
        return ''
    str_data = data.text.strip().replace(LF, EMPTY)
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

FORMAT_LINE = '{teritory}, {url_teritory}, {url_teritory_flag}, {teritory_width}, {teritory_height}, {admin}, {url_admin}, {url_admin_flag}, {admin_width}, {admin_height}, {domestic}, {url_domestic}, {claimant}, {url_claimant}, {population}, {area}, {referendum}, {note}, {url_note} \n'

wdata = ""

with open('United_Nations_list_of_non-self-governing_territories_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
#table = soup.find_all("table")
# print(table)

rows = soup.select("table tr")

for row in rows:
    ths = row.find_all('th')
    len_th = len(ths)
    if len_th > 0:
        continue
    cols = row.find_all('td')
    len_cols = len(cols)
    print('len: ', len_cols)
    teritory = ''
    url_teritory = ''
    url_teritory_flag = ''
    teritory_width = 0
    teritory_height = 0
    if len_cols >= 1:
        teritory, url_teritory = parse_a_img(cols[0])
        url_teritory_flag,  teritory_width, teritory_height = parse_img(cols[0])
        print(teritory)
    admin = ''
    url_admin = ''
    url_admin_flag = ''
    admin_width = 0
    admin_height = 0
    if len_cols >= 2:
        admin, url_admin = parse_a_img(cols[1])
        url_admin_flag, admin_width, admin_height = parse_img(cols[1])
    domestic = ''
    url_domestic = ''
    if len_cols >= 3:
        domestic, url_domestic = parse_a(cols[2])
    claimant = ''
    url_claimant = ''
    if len_cols >= 4:
            claimant, url_claimant = parse_a(cols[3])
    population = ''
    if len_cols >= 5:
            population = parse_text(cols[4])
    area = ''
    if len_cols >= 6:
            area = parse_text(cols[5])    
    referendum = ''
    if len_cols >= 7:
            referendum = strip_ref(cols[6])
    note = ''
    url_note = ''
    if len_cols >= 8:
            note, url_note = parse_a(cols[7])

    line = FORMAT_LINE.format(teritory=teritory, url_teritory=url_teritory, url_teritory_flag=url_teritory_flag, teritory_width =teritory_width, teritory_height =teritory_height, admin=admin, url_admin=url_admin, url_admin_flag=url_admin_flag, admin_width=admin_width, admin_height=admin_height, domestic=domestic, url_domestic=url_domestic, claimant=claimant, url_claimant=url_claimant, population=population, area=area, referendum=referendum, note=note, url_note=url_note)
    print(line)
    wdata += line;

with open('un_non_self_governing_territories.csv', 'w') as f2:
     f2.write(wdata)

