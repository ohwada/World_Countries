# parse_html.py

from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"
  
HTTPS = "https:"

FORMAT_LINE = "{country}, {url_country}, {date}\n"

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

def parse_date(data):
    if not data:
        return ""
    span = data.find("span")
    if not span:
        return ""
    date = span.string
    return date
#

wdata = ""

with open('Member states of the United Nations _table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
#table = soup.find_all("table")
# print(table)

rows = soup.select("table tr")
#print(tr)

for row in rows:
    # print(row)
    th_cols = row.find_all("th")
    td_cols = row.find_all("td")
    # print(cols)
    len_th_cols = len(th_cols)
    len_td_cols = len(td_cols)
    name = ""
    url= "" 
    if len_th_cols >= 1:
        # print(th_cols[0])
        name, url = parse_a(th_cols[0])
        print(name)
    date= ""
    if len_td_cols >= 1:
        print(td_cols[0])
        date = parse_date(td_cols[0])

    line = FORMAT_LINE.format(country=name, url_country=url, date=date)
    print(line)
    wdata += line;

with open('un_countries.csv', 'w') as f2:
     f2.write(wdata)

