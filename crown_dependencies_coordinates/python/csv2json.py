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

dic['title'] = 'List of Crown Dependencies with Coordinates'

dic['desc'] = 'The Crown Dependencies are three flag islands in the British Islands that are self-governing possessions of the British Crown'

dic['reference'] = 'wikipedia: Crown Dependencies'

dic['url_reference'] = 'https://en.wikipedia.org/wiki/Crown_Dependencies'

islands=[]

with open('crown_dependencies_coordinates.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row >= 13:
            d= {}
            d['id'] = int( row[0].strip() )
            d['group'] = int( row[1].strip() )
            d['rowspan'] = int( row[2].strip() )
            d['teritory'] = row[3].strip()
            d['url_teritory'] = row[4].strip()
            d['url_flag'] = row[5].strip()
            d['flag_width'] = int( row[6].strip() )
            d['flag_height'] = int( row[7].strip() )
            d['capital'] = row[8].strip()
            d['url_capital'] = row[9].strip()
            d['island'] = row[10].strip()
            d['url_island'] = row[11].strip()
            d['lat'] = float( row[12].strip() )
            d['lon'] = float( row[13].strip() )
            print(d)
            islands.append(d)
#

dic['islands'] = islands

with open('crown_dependencies_coordinates.json', 'wt') as f2:
    json.dump(dic, f2)
