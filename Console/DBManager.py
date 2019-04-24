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
REFRESH_RATE = 60

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
        
        firebase = pyrebase.initialize_app(config) #initialize firebase storage
        self.db = firebase.database() 
        self.my_prof_slots=[] #list of slots for currently logged in professor

    def login(self, username, password):
        #grabs the entire data base from firebase
        self.full_db = self.db.child('/').get().val()
        
        for prof in self.full_db['professors']:
            if prof['username']==username and prof["password"]==password:   #authentication check for username and password of professor
                self.my_prof = prof
                for slot in self.full_db["slots"].values():
                    if prof['id']==slot["prof_id"]:     #check if the professor's id and the slot-associated professor id are the same
                        self.my_prof_slots.append(slot)                     
                return True
        return False

    def updateDBSlots(self, data):  #to push slot information to the database
        self.db.child('slots').update({data['id']: data})
        self.my_prof_slots.append(data)


    def removeDBSlots(self, data):  #to delete slot information from the database
        self.db.child("slots").child(data['id']).remove()
        self.my_prof_slots.remove(data)


    def reloadSlots(self):  #to refresh slot information from the database
        self.full_db = self.db.child('/').get().val()
        self.my_prof_slots=[]
        for s in self.full_db["slots"].values():
            if self.my_prof['id']==s["prof_id"]:
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



        

    

