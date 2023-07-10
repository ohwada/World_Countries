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

dic['title'] = 'United Nations List of non-self-governing Territories'


dic['desc'] = 'non-self-governing territory as a territory "whose people have not yet attained a full measure of self-government'

dic['reference'] = 'wikipedia: United Nations list of non-self-governing territories'

dic['url_reference'] ='https://en.wikipedia.org/wiki/United_Nations_list_of_non-self-governing_territories'

territories = []

with open('un_non_self_governing_territories.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        len_row = len(row)
        if len_row < 19:
            continue
        d= {}
        d['territory'] = row[0].strip()
        d['url_territory'] = row[1].strip()
        d['url_territory_flag'] = row[2].strip()
        d['territory_width'] = int( row[3].strip() )
        d['territory_height'] = int( row[4].strip() )
        d['admin_state'] = row[5].strip()
        d['url_admin_state'] = row[6].strip()
        d['url_admin_flag'] = row[7].strip()
        d['admin_width'] = int( row[8].strip() )
        d['admin_height'] = int( row[9].strip() )
        d['domestic_legal_status'] = row[10].strip()
        d['url_domestic_legal_status'] = row[11].strip()
        d['other_claimant'] = row[12].strip()
        d['url_other_claimant'] = row[13].strip()
        d['population'] = restore_comma( row[14] )
        d['area'] = row[15].strip()
        d['referendum'] = row[16].strip()
        d['note'] = row[17].strip()
        d['url_note'] = row[18].strip()
        print(d)
        territories.append(d)

dic['territories'] = territories

with open('un_non_self_governing_territories.json', 'wt') as f2:
    json.dump(dic, f2)
