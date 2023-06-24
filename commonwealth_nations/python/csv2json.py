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

dic['title'] = "List of Member states of the Commonwealth of Nations"

dic['desc'] = "The Commonwealth of Nations is a voluntary association of 56 sovereign states. Most of them were British colonies or dependencies of those colonies."

dic['reference'] = "wikipedia: Member states of the Commonwealth of Nations"

dic['url_reference'] ="https://en.wikipedia.org/wiki/Member_states_of_the_Commonwealth_of_Nations"

countries=[]

with open('commonwealth_nations.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()        
        d['date'] = row[2].strip()
        d['region'] = row[3].strip()
        d['url_region'] = row[4].strip()
        d['subregion'] = row[5].strip()
        d['url_subregion'] = row[6].strip()
        d['population'] =  restore_comma(row[7])
        d['government'] = row[8].strip()
        d['notes'] = row[9].strip()
        print(d)
        countries.append(d)

dic['countries'] = countries

with open('commonwealth_nations.json', 'wt') as f2:
    json.dump(dic, f2)
