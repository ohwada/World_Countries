# csv2json.py
# 2023-06-01 K.OHWADA

import csv
import json

dic = {}

dic['title'] = 'List of countries that have gained independence from the United Kingdom'

dic['table_title'] = 'Evolution of Dominions to independence'

dic['desc'] = 'Below are lists of the countries and territories formerly ruled or administered by the United Kingdom or part of the British Empire (including military occupations that did not retain the pre-war central government), with their independence days. Some countries did not gain their independence on a single date, therefore the latest day of independence is shown with a break down of dates further down. A total of 65 countries have claimed their independence from the British Empire or the United Kingdom.'

dic['reference'] = "wikipedia: List of countries that have gained independence from the United Kingdom"

dic['url_reference'] ="https://en.wikipedia.org/wiki/List_of_countries_that_have_gained_independence_from_the_United_Kingdom"

countries=[]

with open('countries_from_uk_dominion.csv') as f1:
    reader = csv.reader(f1)
    for row in reader:
        d= {}
        d['country'] = row[0].strip()
        d['url_country'] = row[1].strip()
        d['url_flag_icon'] = row[2].strip()
        d['icon_width'] = int( row[3].strip() )
        d['icon_height'] = int( row[4].strip() )
        d['date_of_dominion_status'] = row[5].strip()
        d['date_of_adoption_of_statute_of_westminster'] = row[6].strip()
        d['date_of_final_relinquishment_of_british_powers'] = row[7].strip()
        d['final_event_in_question'] = row[8].strip()
        d['url_final_event_in_question'] = row[9].strip()
        d['notes'] = row[7].strip()

        print(d)
        countries.append(d)

dic['countries'] = countries

with open('countries_from_uk_dominion.json', 'wt') as f2:
    json.dump(dic, f2)
