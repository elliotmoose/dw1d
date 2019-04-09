# -*- coding: utf-8 -*-

import datetime
#offset by app
offset = 0

#grab 1st week
today = str(datetime.date.today())
today = today.split('-')
year = today[0]
month = today [1]
date = int(today[2])

#print("Today's date:", str(today))

day = datetime.datetime.today().weekday()

def getcurrentweek(day, date, month, year, offset = 3):
    year = year[2:]
    monday = (date - day) + 7*offset
    for days in range(monday, monday+5):
        if len(str(days)) < 2:
            days = '0'+str(days)
        current_date = '{:2}/{:2}/{:2}'.format(days, month, year)
        print(current_date)
        
getcurrentweek(day, date, month, year)