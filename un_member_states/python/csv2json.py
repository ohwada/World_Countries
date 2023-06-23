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

dic['title'] = "List of Member states of the United Nations"

dic['desc'] ="The member states of the United Nationscomprise 193 sovereign states. The United Nations (UN) is the world's largest intergovernmental organization. All members have equal representation in the UN General Assembly."

dic['reference'] = "wikipedia: Member states of the United Nations"

dic['url_reference'] ="https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

countries=[]

with open('un_members.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()
        d['date'] = row[2].strip()
        d['original_member'] = row[3].strip()
        d['notes'] = restore_comma(row[4])

        print(d)
        countries.append(d)

dic['countries'] = countries

with open('un_members.json', 'wt') as f2:
    json.dump(dic, f2)
