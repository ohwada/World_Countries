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

dic['title'] =  'List of British Overseas Territories with Coordinates'

dic['desc'] = 'The British Overseas Territories are fourteen territories with a constitutional and historical link with the United Kingdom.'

dic['reference'] =  'wikipedia: ritish Overseas Territories'

dic['url_reference'] = 'https://en.wikipedia.org/wiki/British_Overseas_Territories'

territories=[]

with open('british_overseas_territories_coordinates.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['territory'] =  restore_comma( row[0] )
        d['url_territory'] = row[1].strip()
        d['capital'] = row[2].strip()
        d['url_capital'] = row[3].strip()
        d['url_flag'] = row[4].strip()
        d['flag_width'] = int( row[5].strip() )
        d['flag_height'] = int( row[6].strip() )
        d['lat'] = float( row[7].strip() )
        d['lon'] = float( row[8].strip() )
        print(d)
        territories.append(d)

dic['territories'] = territories

with open('british_overseas_territories_coordinates.json', 'wt') as f2:
    json.dump(dic, f2)
