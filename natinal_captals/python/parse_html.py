# parse_html.py
# 2023-06-01 K.OHWADA

from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"
  
HTTPS = "https:"

FORMAT_LINE = "{country}, {url_country}, {capital}, {url_capital}, {url_flag}, {width}, {height}, {notes}\n"

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

wdata = ""

with open('List of national capitals_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
#table = soup.find_all("table")
# print(table)

rows = soup.select("table tr")
#print(tr)

for row in rows:
    print(row)
    cols = row.find_all("td")
    print(cols)
    len_cols = len(cols)
    print("len", len_cols)
    name0 = ""
    url0= "" 
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
        notes = cols[2].string
        print(notes)
    line = FORMAT_LINE.format(country=name1, url_country=url1, capital=name0, url_capital=url0, url_flag=img_url, width =width, height= height, notes=notes)
    print(line)
    wdata += line;

with open('captals.csvl', 'w') as f2:
     f2.write(wdata)

