# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

COMMA = ','

COMMA_HTML = '&comma;'

HYPHON = '-'

EMPTY = ''

def  restore_comma(data):
    if not data:
        return ""
    str_data = data.strip()
    ret = str_data.replace(COMMA_HTML, COMMA)
    return ret
#

def get_url_station_flag(data):
    if not data:
        return EMPTY
    str_data = data.strip()
    if str_data == HYPHON:
        return EMPTY
    return str_data
#

dic = {}

dic['title'] = 'List of Research stations in Antarctica with Coordinates'

dic['desc'] = 'the research stations of the Antarctic are constructed either on rock or on ice that is (for practical purposes) fixed in place. Many of the stations are staffed throughout the year.  A total of 42 countries (as of October 2006), all signatories to the Antarctic Treaty, operate seasonal (summer) and year-round research stations on the continent. '

dic['reference'] = 'wikipedia: Research stations in Antarctica'

dic['url_reference'] =  'https://en.wikipedia.org/wiki/Research_stations_in_Antarctica'

stations=[]

with open('antarctic_research_stations_coordinates.csv') as f1:
    reader = csv.reader(f1)

    for row in reader:
        len_row = len(row)
        print('len: ', len_row)
        if len_row < 13:
            continue
        d= {}
        d['station'] = row[0].strip()
        d['url_station'] = row[1].strip()
        d['url_station_flag'] = get_url_station_flag( row[2] )
        d['station_width'] = int( row[3].strip() )
        d['station_height'] = int( row[4].strip() )
        d['location'] = row[5].strip()
        d['url_location'] = row[6].strip()
        d['country'] = row[7].strip()
        d['url_country_flag'] =  row[8].strip()
        d['country_width'] = int( row[9].strip() )
        d['country_height'] = int( row[10].strip() )
        d['lat'] = float( row[11].strip() )
        d['lon'] = float( row[12].strip() )
        print(d)
        stations.append(d)
#

dic['stations'] = stations

with open('antarctic_research_stations_coordinates.json', 'wt') as f2:
    json.dump(dic, f2)
