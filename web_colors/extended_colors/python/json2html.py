# json2html.py
# 2023-06-01 K.OHWADA

import json


FORMAT_BOX = '<div class="box" style="background-color: {hex_rgb}">'

FORMAT_A_TAG = '<a href="{href}">{name}</a>'


with open('template_html.txt', 'r') as f1:
    template_html = f1.read()

with open('template_row.txt', 'r') as f2:
    template_row = f2.read()

colors =[]

rows= ''

with open('css_extended_colors_147.json') as f3:
    dic = json.load(f3)
#

str_title = dic['title']
desc = dic['desc']
ref = dic['reference']
url_ref = dic['url_reference']
list_colors = dic['colors']
  
 
for item in list_colors:
    name = item['name']
    hex_rgb = item['hex']
    box = FORMAT_BOX .format(hex_rgb=hex_rgb)
    row = template_row.format(name =name, hex_rgb=hex_rgb, box=box)
    print(row)
    rows +=  row
#

html_ref = FORMAT_A_TAG.format(href=url_ref, name=ref)

wdata = template_html.format(body_title=str_title, desc=desc, rows=rows, reference=html_ref)
  
with open('css_extended_colors_147.html', 'w') as f4:
    f4.write(wdata)
#



