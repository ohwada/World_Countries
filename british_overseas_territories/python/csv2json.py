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

dic['reference'] = "wikipedia: British Overseas Territories"

dic['url_reference'] =" https://en.wikipedia.org/wiki/British_Overseas_Territories"

territories=[]

with open('british_overseas_territories.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['territory'] =  restore_comma( row[0] )
        d['url_territory'] = row[1].strip()
        d['url_flag'] = row[2].strip()
        d['flag_width'] = int( row[3].strip() )
        d['flag_height'] = int( row[4].strip() )
        d['url_arms'] = row[5].strip()
        d['arms_width'] = int( row[6].strip() )
        d['arms_height'] = int( row[7].strip() )
        d['location'] = restore_comma( row[8] )
        d['url_location'] = row[9].strip()
        d['motto'] = restore_comma( row[10] )
        d['area'] = restore_comma( row[11] )
        d['population'] = restore_comma( row[12] )
        d['capital'] = row[13].strip()
        d['url_capital'] = row[14].strip()
        d['gdp'] = restore_comma( row[15] )
        d['gdp_per_capita'] = restore_comma( row[16] )
        d['notes'] = restore_comma( row[17] )

        print(d)
        territories.append(d)

dic['territories'] = territories

with open('british_overseas_territories.json', 'wt') as f2:
    json.dump(dic, f2)
