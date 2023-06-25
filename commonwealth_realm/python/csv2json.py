# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

COMMA = ','

COMMA_HTML = '&comma;'

def  restore_comma(data):
    if not data:
        return ""
    str_data = data.strip()
    ret = str_data.replace(COMMA_HTML, COMMA)
    return ret
#

dic = {}

dic['title'] = "List of Commonwealth realm"

dic['desc'] = "A Commonwealth realm is a sovereign state that has King of United Kingdom (Charles III) as its monarch and head of state. "

dic['reference'] = "wikipedia: Commonwealth realm"

dic['url_reference'] ="https://en.wikipedia.org/wiki/Commonwealth_realm"

countries=[]

with open('commonwealth_realm .csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()
        d['population'] =  restore_comma(row[2])
        d['year'] = row[3].strip()
        d['governor'] = row[4].strip()
        d['url_governor'] = row[5].strip()
        d['prime_minister'] = row[6].strip()
        d['url_prime_minister'] = row[7].strip()

        print(d)
        countries.append(d)

dic['countries'] = countries

with open('commonwealth_realm.json', 'wt') as f2:
    json.dump(dic, f2)
