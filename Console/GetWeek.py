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

#test getWeek function, just run
a = (getWeek(offset))
# print(a)

#This function creates a list of lists which indexes correspond to the day
#The nested lists contain 20 dictionaries of time slots from 08:00 to 18:00 in 30min intervals 
def getButtons(weeklist):
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
            slots['time'] = '{}:{}'.format(hour, minutes)
            slots['date'] = weeklist[i]
            slots['id'] = str(uuid.uuid1())
            days.append(slots)
        output.append(days)
        
    return output

print(getButtons(a))
            
            
        


