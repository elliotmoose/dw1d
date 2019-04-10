import dateutil.relativedelta as rdelta
import datetime as DT

#global today and day variables
today = DT.date.today()  # today's date
day = DT.datetime.today().weekday() #which day today is

#variable offset
offset = 3



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
print (getWeek(offset))



