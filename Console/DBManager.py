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
   
        
    def login(self, username, password):
        full_db = self.db.child('/').get().val()
        
        #username="John"#change accordingly
        #password="password"#change accordingly
        
        self.my_prof_slots=[]
        #allslots = full_db['slots']
        for p in full_db['professors']:
        
            if p['username']==username and p["password"]==password:
                self.my_prof = p
                for s in full_db["slots"].values():
                    if p['id']==s["prof_id"]:
                    #print(full_db["slots"])
                        self.my_prof_slots.append(s)
                return True
        return False

    def updateDbSlots(self, data):
        print(data)
        #self.db.child('slots').update(data)

