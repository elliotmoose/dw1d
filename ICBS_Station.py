import RPi.GPIO as GPIO
import SimpleMFRC522 #RFID Library for python
from time import sleep #to control the pace of the code
import pyrebase

reader = SimpleMFRC522.SimpleMFRC522()

FIREBASE_ENDPOINT = 'https://basic-dc724.firebaseio.com/'

config = {
  "apiKey": "AIzaSyByqBZnJMeBo9CjNn111hRYWo34ipRIOwM",
  "authDomain": "basic-dc724.firebaseapp.com",
  "databaseURL": "https://basic-dc724.firebaseio.com/",
  "storageBucket": "basic-dc724.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()  
print("Tap your ID card")

try:
    while True:
        status, TagType = reader.read_no_block()
        
        if status != None:            
            print(status)
            if db.child('current').get().val() != None: #someone is using the station. Do not override
                print('Error: User in session. Please log out first')
                sleep(1)
                continue
            
            allstudents = db.child('students').get().val()
            
            for student in allstudents.values():
                if student['can_number'] == str(status): #find a student with the same can number
                    db.child('/').update({'current':student}) #if same, set current as this student
                    print('Found and logged in student: {0}'.format(student['name']))
                    sleep(1)
                    continue

        sleep(0.1)

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()    

