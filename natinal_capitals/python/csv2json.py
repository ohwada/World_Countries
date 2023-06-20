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

dic['title'] ="List of National Capitals"

dic['desc'] ="This is a list of national capitals, including capitals of territories and dependencies, non-sovereign states including associated states and entities whose sovereignty is disputed."

dic['reference'] ="wikipedia: List_of_national_capitals"

dic['url_reference'] ="https://en.wikipedia.org/wiki/List_of_national_capitals"

countries=[]

with open('captals.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        len_row = len(row)
        print("len:", len_row)
        d= {}
        if len_row >= 8:
            d['country'] = row[0].strip()
            d['url_country'] = row[1].strip()
            d['capital'] =  restore_comma(row[2])
            d['url_capital'] = row[3].strip()
            d['url_flag'] = row[4].strip()
            d['width'] = int( row[5].strip() )
            d['height'] = int( row[6].strip() )
            d['notes'] =  restore_comma(row[7])
            print(d)
            countries.append(d)

dic['countries'] = countries

with open('capitals.json', 'wt') as f2:
    json.dump(dic, f2)
