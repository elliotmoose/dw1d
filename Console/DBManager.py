"""
The purpose of DB manager is to handle all interactions with the database

i.e. 
1. Receiving Logins
2. Loading data for a login 
    a. subjects for student
    b. professors for that subject
    c. slots for that professor

"""
# import time

# class DBManager:        
#     def __init__(self):
#         self.loggedIn = False
#         self.data = {}
        
#     def login(self, username, password):
#         if username=='elliot' and password=='12345':
#             return True, {'data': 'test data'}
#         else:
#             return False, None

#     def logout(self):
#         self.loggedIn = False
#         self.data = {}    
#         # self.beginCheckLoginCycle()  
           
import time
from threading import Timer
from libdw import pyrebase
#import TemplateData
import copy

FIREBASE_ENDPOINT = 'https://basic-dc724.firebaseio.com/'
REFRESH_RATE = 60 #firebase calls are still a bottleneck

config = {
  "apiKey": "AIzaSyByqBZnJMeBo9CjNn111hRYWo34ipRIOwM",
  "authDomain": "basic-dc724.firebaseapp.com",
  "databaseURL": "https://basic-dc724.firebaseio.com/",
  "storageBucket": "basic-dc724.appspot.com"
}

class DBManager:        
    def __init__(self):
        self.loggedIn = False
        self.data = {}
        
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database() 

        self.full_data = {}

        self.my_prof_slots=[]

   
        
    def login(self, username, password):
        self.full_db = self.db.child('/').get().val()
        
        #username="John"#change accordingly
        #password="password"#change accordingly
        
        #allslots = full_db['slots']
        self.my_prof_slots=[]

        for p in self.full_db['professors']:
        
            if p['username']==username and p["password"]==password:
                self.my_prof = p
                for s in self.full_db["slots"].values():
                    if p['id']==s["prof_id"]:
                    #print(full_db["slots"])
                        self.my_prof_slots.append(s)
                return True
        return False

    def updateDBSlots(self, data):
        print(data)
        self.db.child('slots').update({data['id']: data})
        self.my_prof_slots.append(data)


    def removeDBSlots(self, data):
        self.db.child("slots").child(data['id']).remove()
        self.my_prof_slots.remove(data)


    def reloadSlots(self):
        self.full_db = self.db.child('/').get().val()
        self.my_prof_slots=[]
        for s in self.full_db["slots"].values():
            if self.my_prof['id']==s["prof_id"]:
            #print(full_db["slots"])
                self.my_prof_slots.append(s)


    #returns tuple: (success, message)
    def allocate_credits(self, student_id, amount):
        students = self.db.child('students').get().val()

        for student in students.values():
            if student['id'] == student_id:
                self.db.child('students').child(student['id']).update({
                    'credits': student['credits'] + amount
                })

                return True, ''

        return False, 'Could not find a\nstudent with ID:\n{}'.format(student_id)



        

    

