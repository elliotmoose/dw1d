import time
import datetime

seconds_in_week = 60*60*24*7

now = time.time() #epoch time of now

dayOfWeek = datetime.datetime.fromtimestamp(now).weekday()
print (dayOfWeek)
isThursday = dayOfWeek == 3
isFriday = dayOfWeek == 4

if isThursday or isFriday: #If it is a thursday or a friday, we want to get the last monday
    monday = (now // seconds_in_week) * seconds_in_week - 3*60*60*24
else: #Else we want to get next monday
    monday = (now // seconds_in_week) * seconds_in_week + 4*60*60*24



x = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(monday))
x = x.split(' ')[0]
print(x)


