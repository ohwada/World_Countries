# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] = "List of Member states of the United Nations with National Flag"

dic['desc'] ="The member states of the United Nationscomprise 193 sovereign states. The United Nations (UN) is the world's largest intergovernmental organization. All members have equal representation in the UN General Assembly."

dic['reference'] = "wikipedia: Member states of the United Nations"

dic['url_reference'] ="https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

countries=[]

with open('un_countries_flag.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['offical_name'] = row[1].strip()
        d['url_country'] = row[2].strip()
        d['date'] = row[3].strip()
        d['url_flag_icon'] = row[4].strip()
        d['icon_width'] = int( row[5].strip() )
        d['icon_height'] = int( row[6].strip() )
        d['url_flag'] = row[7].strip()
        d['flag_width'] = int( row[8].strip() )
        d['flag_height'] = int( row[9].strip() )

        print(d)
        countries.append(d)

dic['countries'] = countries

with open('un_countries_flag.json', 'wt') as f2:
    json.dump(dic, f2)
