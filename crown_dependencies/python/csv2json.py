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

dic['title'] = 'List of Crown Dependencies'

dic['desc'] = 'The Crown Dependencies are three flag islands in the British Islands that are self-governing possessions of the British Crown'

dic['reference'] = 'wikipedia: Crown Dependencies'

dic['url_reference'] = 'https://en.wikipedia.org/wiki/Crown_Dependencies'

islands=[]

with open('crown_dependencies.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row >= 21:
            d= {}
            d['id'] = int (row[0].strip() )
            d['group'] = int (row[1].strip() )
            d['rowspan'] = int (row[2].strip() )
            d['territory'] = row[3].strip()
            d['url_territory'] = row[4].strip()
            d['location'] = row[5].strip()
            d['url_location'] = row[6].strip()
            d['monarch'] = row[7].strip()
            d['url_monarch'] = row[8].strip()
            d['area'] = row[9].strip()
            d['population'] = restore_comma( row[10] )
            d['url_flag'] = row[11].strip()
            d['flag_width'] = int( row[12].strip() )
            d['flag_height'] = int( row[13].strip() )
            d['url_arms'] = row[14].strip()
            d['arms_width'] = int( row[15].strip() )
            d['url_arms_height'] = int( row[16].strip() )
            d['capital'] = row[17].strip()
            d['url_capital'] = row[18].strip()
            d['airport'] = row[19].strip()
            d['url_airport'] = row[20].strip()
            print(d)
            islands.append(d)

dic['islands'] = islands

with open('crown_dependencies.json', 'wt') as f2:
    json.dump(dic, f2)
