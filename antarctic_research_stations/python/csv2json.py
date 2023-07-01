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

dic['title'] = 'List of Research stations in Antarctica'

dic['desc'] = 'the research stations of the Antarctic are constructed either on rock or on ice that is (for practical purposes) fixed in place. Many of the stations are staffed throughout the year.  A total of 42 countries (as of October 2006), all signatories to the Antarctic Treaty, operate seasonal (summer) and year-round research stations on the continent. '

dic['reference'] = 'wikipedia: Research stations in Antarctica'

dic['url_reference'] =  'https://en.wikipedia.org/wiki/Research_stations_in_Antarctica'

stations=[]

with open('antarctic_research_stations.csv') as f1:
    reader = csv.reader(f1)

    for row in reader:
        d= {}
        d['station'] = row[0].strip()
        d['url_station'] = row[1].strip()
        d['location'] = row[2].strip()
        d['url_location'] = row[3].strip()
        d['country'] = row[4].strip()
        d['url_country_flag'] = row[5].strip()
        d['country_width'] = int( row[6].strip() )
        d['country_height'] = int( row[7].strip() )
        d['admin'] = row[8].strip()
        d['url_admin'] = row[9].strip()
        d['yearest'] = row[10].strip()
        d['max_pers'] = row[11].strip()
        d['summer_pop'] = row[12].strip()
        d['winter_pop'] = row[13].strip()
        d['locode'] = row[14].strip()
        d['utc_offset'] = row[15].strip()
        d['url_utc_offset'] = row[16].strip()
        d['mean_annual_temp'] = row[17].strip()
        print(d)
        stations.append(d)
#

dic['stations'] = stations

with open('antarctic_research_stations.json', 'wt') as f2:
    json.dump(dic, f2)
