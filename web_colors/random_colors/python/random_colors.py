# random_colors.py
# 2023-06-01 K.OHWADA


import json
import random


FORMAT_COL = '<td><div class="box" style="background-color: {hex_rgb}" onclick="alert(\'{name}\')" /></td> \n'

str_title = 'Random Colors 64'

desc = 'pick 64 random colors from Web Color 100'

with open('template_html_random.txt', 'r') as f1:
    template_html = f1.read()
#


with open('web_colors_100.json') as f2:
    dic = json.load(f2)
#

list_colors = dic['colors']

len_list = len( list_colors)

rows = ''

for i in range(8):
    cols = '<tr>'
    for j in range(8):
        rint = random.randint(0, (len_list -1) )
        item = list_colors[rint]
        name = item['name']
        hex_rgb = item['hex']
        col = FORMAT_COL .format(name=name, hex_rgb=hex_rgb)
        cols += col

    row = cols + '</tr> \n'
    rows += row
#

wdata = template_html.format(body_title=str_title, desc=desc, rows=rows)
  
with open('random_colors_64.html', 'w') as f3:
    f3.write(wdata)
#


