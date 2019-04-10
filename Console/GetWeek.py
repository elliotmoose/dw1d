# -*- coding: utf-8 -*-
#
#import datetime
#from calendar import monthrange
##offset by app
#offset = 0
##print("Today's date:", str(today))
#
#def getcurrentweek(offset):
#    #grab current values
#
##    number_of_days_current_month = monthrange(int(year), int(month)[1]
#    output = []
#    year = year[2:]
#    monday = (date - day) + 7*offset
#    for days in range(monday, monday+5):
#        if len(str(days)) < 2:
#            days = '0'+str(days)
##        if days > number_of_days_current_month:
#            
#        current_date = '{:2}/{:2}/{:2}'.format(days, month, year)
#        output.append(current_date)
#    return output
#
#print(getcurrentweek(offset))

import dateutil.relativedelta as rdelta
import datetime as DT

today = DT.date.today()  # today's date
day = DT.datetime.today().weekday() #which day today is
#print(day)
#print(today)
offset = 3

if offset == 0:
    idx1 = -1
    idx2 = 1
else:
    idx1 = offset
    idx2 = offset + 1
    
def mon(a):
    monday = today + rdelta.relativedelta(weekday=rdelta.MO(a))
    return monday

def tue(a):
    tuesday = today + rdelta.relativedelta(weekday=rdelta.TU(a)) 
    return tuesday

def wed(a):
    wednesday = today + rdelta.relativedelta(weekday=rdelta.WE(a))
    return wednesday
   
def thu(a):
    thursday = today + rdelta.relativedelta(weekday=rdelta.TH(a))
    return thursday

def fri(a):
    friday = today + rdelta.relativedelta(weekday=rdelta.FR(a))
    return friday

out1 = [mon(idx1), tue(idx1), wed(idx1), thu(idx1), fri(idx1)]
out2 = [mon(idx2), tue(idx2), wed(idx2), thu(idx2), fri(idx2)]
output = out1[:day]+out2[day:] 
for i in range(len(output)):
    output[i] = str(output[i])

print(output)



