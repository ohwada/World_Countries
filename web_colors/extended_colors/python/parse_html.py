# parse_html.py
# 2023-06-01 K.OHWADA

from bs4 import BeautifulSoup


COMMA = ','

COMMA_HTML = '&comma;'

COMMA_URL = '%2c'

def parse_text(data):
    if not data:
        return ""
    str_data = data.text.strip()
    ret = str_data.replace(COMMA, COMMA_HTML)
    return ret
#


FORMAT_LINE = '{name}, {hex_rgb} \n'

wdata =  ''

with open('CSS_Propertie_color_keywords_extended_table.html', 'r') as f1:
     html = f1.read()
  
soup = BeautifulSoup(html,'html.parser')
    
rows = soup.select("table tr")

for row in rows:
    cols = row.find_all("td")
    len_cols = len(cols)
    if len_cols < 4:
        continue
    name = ''
    if len_cols >= 3:
        name = parse_text(cols[2])
    hex_rgb = ''
    if len_cols >= 4:
        hex_rgb = parse_text(cols[3])

    line = FORMAT_LINE.format(name=name, hex_rgb=hex_rgb)
    print(line)
    wdata += line;

with open('css_extended_colors.csv', 'w') as f2:
     f2.write(wdata)

