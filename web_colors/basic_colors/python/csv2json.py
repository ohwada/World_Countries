# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] = 'CSS Basic Colors 16'

dic['desc'] = '16 Basic Colors that can be used in CSS'

dic['reference'] = 'W3C: CSS/Properties/color/keywords'

dic['url_reference'] = 'https://www.w3.org/wiki/CSS/Properties/color/keywords'

colors =[]

with open('css_basic_colors.csv') as f1:
    reader = csv.reader(f1)
    
    for row in reader:
        len_row = len(row)
        if len_row < 2:
            continue
        d= {}
        d['name'] = row[0].strip()
        d['hex'] = row[1].strip()
        print(d)
        colors.append(d)
#

dic['colors'] = colors

with open('css_basic_colors_16.json', 'wt') as f2:
    json.dump(dic, f2)
