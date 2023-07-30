# -*- coding: utf-8 -*-
# parse_html.py
# 2023-06-01 K.OHWADA


from bs4 import BeautifulSoup


FILE_HTML = 'shitei_toshi_ichiran_table.html'

FILE_CSV = 'shitei_toshi_ichiran.csv'


COMMA = ','

COMMA_HTML = '&comma;'

LF = '\n'

LF_HTML = '&#010;'

EMPTY = ''

SPACE = ' '

HYPHEN = '-'


def parse_text(data):
    if not data:
        return ''
    str1 = data.text.strip()
    str2 = str1.replace(COMMA, COMMA_HTML)
    ret = str2.replace(LF,  LF_HTML)
    return ret
#


FORMAT_LINE = "{name}, {population}, {date}, {decree} \n"

wdata = ""


with open(FILE_HTML, 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
#table = soup.find_all("table")
# print(table)

rows = soup.select("table tr")
#print(tr)

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    if len_cols < 3:
        continue
    name = EMPTY
    if len_cols >= 1:
        name = parse_text(cols[0])
        print(name)
    population = EMPTY
    if len_cols >= 2:
         population = parse_text(cols[1])
    date= EMPTY
    if len_cols >= 3:
        date = parse_text(cols[2])
    decree= HYPHEN
    if len_cols >= 4:
        decree = parse_text(cols[3])
    line = FORMAT_LINE.format(name=name, population=population, date=date, decree=decree)
    print(line)
    wdata += line;
#


with open(FILE_CSV, 'wt') as f2:
     f2.write(wdata)
#

