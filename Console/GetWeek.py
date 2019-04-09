# -*- coding: utf-8 -*-

import datetime
from calendar import monthrange
#offset by app
offset = 4
#print("Today's date:", str(today))

def getcurrentweek(offset):
    #grab current values
    today = str(datetime.date.today())
    today = today.split('-')
    year = today[0]
    month = today [1]
    date = int(today[2])
    day = datetime.datetime.today().weekday()
#    number_of_days_current_month = monthrange(int(year), int(month)[1]
    output = []
    year = year[2:]
    monday = (date - day) + 7*offset
    for days in range(monday, monday+5):
        if len(str(days)) < 2:
            days = '0'+str(days)
#        if days > number_of_days_current_month:
            
        current_date = '{:2}/{:2}/{:2}'.format(days, month, year)
        output.append(current_date)
    return output

print(getcurrentweek(offset))

