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

dic['title'] = "List of British Overseas Territories"

dic['desc'] ="The British Overseas Territories are fourteen territories with a constitutional and historical link with the United Kingdom."

dic['reference'] = "wikipedia: ritish Overseas Territories"

dic['url_reference'] =" https://en.wikipedia.org/wiki/British_Overseas_Territories"

teritories=[]

with open('british_territories.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['teritory'] =  restore_comma( row[0] )
        d['url_teritory'] = row[1].strip()
        d['capital'] = row[2].strip()
        d['url_capital'] = row[3].strip()
        d['url_flag'] = row[4].strip()
        d['flag_width'] = int( row[5].strip() )
        d['flag_height'] = int( row[6].strip() )
        d['url_arms'] = row[7].strip()
        d['arms_width'] = int( row[8].strip() )
        d['arms_height'] = int( row[9].strip() )
        d['location'] = restore_comma( row[10] )
        d['motto'] = restore_comma( row[11] )
        d['area'] = restore_comma( row[12] )
        d['population'] = restore_comma( row[13] )
        d['gdp'] = restore_comma( row[14] )
        d['gdp_per_capita'] = restore_comma( row[15] )
        d['notes'] = restore_comma( row[16] )

        print(d)
        teritories.append(d)

dic['teritories'] = teritories

with open('british_territories.json', 'wt') as f2:
    json.dump(dic, f2)
