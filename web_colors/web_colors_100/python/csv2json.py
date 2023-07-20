# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] = 'Web Colors 100'

dic['desc'] = '100 Colors,exclude Black White and Gray strains from CSS Color Name 147'

dic['reference'] = 'W3C: CSS/Properties/color/keywords'

dic['url_reference'] = 'https://www.w3.org/wiki/CSS/Properties/color/keywords'

colors =[]

with open('web_colors_100.csv') as f1:
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

with open('web_colors_100.json', 'wt') as f2:
    json.dump(dic, f2)
