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

dic['title'] = 'United Nations List of non-self-governing Territories with Coordinates'

dic['desc'] = 'non-self-governing territory as a territory "whose people have not yet attained a full measure of self-government'

dic['reference'] = 'wikipedia: United Nations list of non-self-governing territories'

dic['url_reference'] ='https://en.wikipedia.org/wiki/United_Nations_list_of_non-self-governing_territories'

teritories=[]

with open('un_non_self_governing_territories_coordinates.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['teritory'] = row[0].strip()
        d['url_teritory'] = row[1].strip()
        d['url_teritory_flag'] = row[2].strip()
        d['teritory_width'] = int( row[3].strip() )
        d['teritory_height'] = int( row[4].strip() )
        d['admin_state'] = row[5].strip()
        d['url_admin_state'] = row[6].strip()
        d['url_admin_flag'] = row[7].strip()
        d['admin_width'] = int( row[8].strip() )
        d['admin_height'] = int( row[9].strip() )
        d['lat'] =  float( row[10].strip() )
        d['lon'] =  float( row[11].strip() )
        print(d)
        teritories.append(d)

dic['teritories'] = teritories

with open('un_non_self_governing_territories_coordinates.json', 'wt') as f2:
    json.dump(dic, f2)
