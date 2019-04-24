"""
The purpose of DB manager is to handle all interactions with the database

i.e. 
1. Receiving Logins
2. Loading data for a login 
    a. subjects for student
    b. professors for that subject
    c. slots for that professor

"""          

from libdw import pyrebase

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
        #creates attributes
        self.loggedIn = False
        self.data = {}
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database() 
        self.full_data = {}
        self.my_prof_slots=[]

        
    def login(self, username, password):
        #grabs the entire data base from firebase
        self.full_db = self.db.child('/').get().val()
        self.my_prof_slots=[]

        for p in self.full_db['professors']:
        
            if p['username']==username and p["password"]==password:
                self.my_prof = p
                for s in self.full_db["slots"].values():
                    if p['id']==s["prof_id"]:
                        self.my_prof_slots.append(s)
                return True
        return False

    #adds new available slot that students are able to book
    def updateDBSlots(self, data):
        print(data)
        self.db.child('slots').update({data['id']: data})
        self.my_prof_slots.append(data)

    #removes the slot from database if prof wants to state that he is no longer available during that time slot
    def removeDBSlots(self, data):
        self.db.child("slots").child(data['id']).remove()
        self.my_prof_slots.remove(data)

    #update the my_prof_slots 
    def reloadSlots(self):
        self.full_db = self.db.child('/').get().val()
        self.my_prof_slots=[]
        for s in self.full_db["slots"].values():
            if self.my_prof['id']==s["prof_id"]:
                self.my_prof_slots.append(s)

    

