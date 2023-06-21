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

dic['title'] = "List of Sovereign States"

dic['desc'] ="The following is a list providing an overview of sovereign states around the world with information on their status and recognition of their sovereignty. The 206 listed states can be divided into three categories based on membership within the United Nations System: 193 UN member states, 2 UN General Assembly non-member observer states, and 11 other states."

dic['reference'] ="wikipedia: List of sovereign states"

dic['url_reference'] ="https://en.wikipedia.org/wiki/List_of_sovereign_states"

countries=[]

with open('sovereign_states.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        len_row = len(row)
        print("len:", len_row)
        if len_row >= 9:
            d['country'] = row[0].strip()
            d['formal_name'] = row[1].strip()
            d['url_country'] = row[2].strip()
            d['url_flag'] = row[3].strip()
            d['width'] = int( row[4].strip() )
            d['height'] = int( row[5].strip() )
            d['membership'] =  row[6].strip()
            d['dispute'] = row[7].strip()
            d['info'] =   restore_comma(row[8])
            print(d)
            countries.append(d)

dic['countries'] = countries

with open('sovereign_states.json', 'wt') as f2:
    json.dump(dic, f2)
