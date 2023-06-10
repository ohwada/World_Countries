# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] ="List of national capitals"

dic['desc'] ="This is a list of national capitals, including capitals of territories and dependencies, non-sovereign states including associated states and entities whose sovereignty is disputed."

dic['url_reference'] ="https://en.wikipedia.org/wiki/List_of_national_capitals"

countries=[]

with open('captals.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()
        d['capital'] = row[2].strip()
        d['url_capital'] = row[3].strip()
        d['url_flag'] = row[4].strip()
        d['width'] = row[5].strip()
        d['height'] = row[6].strip()
        d['notes'] = row[7].strip()
        print(d)
        countries.append(d)

dic['countries'] = countries

with open('capitals.json', 'wt') as f2:
    json.dump(dic, f2)
