import dateutil.parser as dateParser
from dateutil.parser import parserinfo
from datetime import datetime

def DateStringToEpoch(date_string):
    return dateParser.parse(date_string,parserinfo(dayfirst=True)).timestamp()

def DateTimeStringToEpoch(date_time_string):
    return dateParser.parse(date_time_string,parserinfo(dayfirst=True)).timestamp()    

def DateStringToDay(date_string):
    return ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',][dateParser.parse(date_string,parserinfo(dayfirst=True)).weekday()]

if __name__ == '__main__':    
    d1 = DateStringToEpoch('02/04/19')    
    d2 = DateTimeStringToEpoch('24/04/19 0800')    
    print(d1)

    