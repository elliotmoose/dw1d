import dateutil.relativedelta as rdelta
import datetime as DT
import uuid
#global today and day variables
today = DT.date.today()  # today's date
day = DT.datetime.today().weekday() #which day today is

#variable offset (feel free to change)
offset = 0

def getWeek(offset):
    #takes into account case of 1st page den following pages
    if offset == 0:
        idx1 = -1
        idx2 = 1
    else:
        idx1 = offset
        idx2 = offset + 1
        
    out1 = [mon(idx1), tue(idx1), wed(idx1), thu(idx1), fri(idx1)]
    out2 = [mon(idx2), tue(idx2), wed(idx2), thu(idx2), fri(idx2)]
    output = out1[:day]+out2[day:] 
    for i in range(len(output)):
        output[i] = str(output[i])
    
    return output

#functions to generate each day    
def mon(a):
    monday = str(today + rdelta.relativedelta(weekday=rdelta.MO(a)))
    output = monday[8:10]+'/'+monday[5:7]+'/'+monday[2:4]
    return output

def tue(a):
    tuesday = str(today + rdelta.relativedelta(weekday=rdelta.TU(a)))
    output = tuesday[8:10]+'/'+tuesday[5:7]+'/'+tuesday[2:4]
    return output

def wed(a):
    wednesday = str(today + rdelta.relativedelta(weekday=rdelta.WE(a)))
    output = wednesday[8:10]+'/'+wednesday[5:7]+'/'+wednesday[2:4]
    return output
   
def thu(a):
    thursday = str(today + rdelta.relativedelta(weekday=rdelta.TH(a)))
    output = thursday[8:10]+'/'+thursday[5:7]+'/'+thursday[2:4]
    return output

def fri(a):
    friday = str(today + rdelta.relativedelta(weekday=rdelta.FR(a)))
    output = friday[8:10]+'/'+friday[5:7]+'/'+friday[2:4]
    return output

#test getWeek function, just run
a = (getWeek(offset))
#print(a)

#This function creates a list of lists which indexes correspond to the day
#The nested lists contain 20 dictionaries of time slots from 08:00 to 18:00 in 30min intervals 
def getButtons(weeklist, profid):
    output = []
    for i in range(5):
        hours = 7
        days = []
        for j in range(21):
            slots = {}
            if j%2 == 0:
                minutes = '00'
                hours += 1
            else:
                minutes = '30'
            hour = str(hours)
            if len(hour) == 1:
                hour = '0' + hour
            slots['time'] = '{}{}'.format(hour, minutes)
            slots['date'] = weeklist[i]
            #slots['id'] = slots['time'] + slots['date']
            slots['prof_id'] = profid
            slots['student_id'] = 'null'
            days.append(slots)
        output.append(days)
        
    return output

#print(getButtons(a))
            
            
        


