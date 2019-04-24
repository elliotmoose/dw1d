import dateutil.parser as dateParser
from dateutil.parser import parserinfo
from datetime import datetime

def DateStringToEpoch(date_string):
    return dateParser.parse(date_string,parserinfo(dayfirst=True)).timestamp()

def DateTimeStringToEpoch(date_time_string):
    return dateParser.parse(date_time_string,parserinfo(dayfirst=True)).timestamp()    

def DateStringToDay(date_string):
    return ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',][dateParser.parse(date_string,parserinfo(dayfirst=True)).weekday()]

def TodayEpoch():
    return datetime.now().timestamp()


import time
if __name__ == '__main__':    
    
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datetime.now().timestamp())))

    