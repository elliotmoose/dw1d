"""
The purpose of DB manager is to handle all interactions with the database

i.e. 
1. Receiving Logins
2. Loading data for a login 
    a. subjects for student
    b. professors for that subject
    c. slots for that professor

"""
import time
from threading import Timer
import pyrebase
import TemplateData
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
    def __init__(self, loginCallback=None):
        self.loggedIn = False
        self.data = {}        
        self.loginCallback = loginCallback
        
        #connect
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()                
    
    def cleanup(self):
        print('Cleaning Up...')
        self.cleanup = True

    def InitalizeFirebase(self):

        confirmed = input('Warning: Initializing removes all current data. Continue? y/n\n')
        
        if confirmed != 'y':
            return

        print('Initializing database...')

        shouldLoginStudent = input('Include template \'current\' student user? y/n\n')

        data = TemplateData.loggedindbtemplate if shouldLoginStudent else TemplateData.dbtemplate
        
        self.db.update(data)
        
        print('Initializing done!')

    def login(self, data):
        self.loggedIn = True
        self.data = data

        print('USER LOGGED IN')        

        if self.loginCallback != None:
            self.loginCallback(data)

    def logout(self):
        self.db.child('current').remove()
        self.loggedIn = False
        self.data = {}    
        self.beginCheckLoginCycle() 
           
    def beginCheckLoginCycle(self):
        t = Timer(1/REFRESH_RATE, self._beginCheckLoginCycle)
        t.start()        
 
    #this is an internal function because it has to be run with a timer (so that it is multithreaded)
    def _beginCheckLoginCycle(self):
        
        #if it is logged in, no more need to check
        if self.loggedIn or self.cleanup == True:
            return

        print('Reading from firebase..')

        #get current student (logged in)
        current = self.db.child('current').get().val()
        if current != None:            
            full_db = self.db.get().val()
            structured_data = self.structure_data(full_db, current)
            self.login(structured_data)
            return

        #call itself to keep checking database
        time.sleep(1/REFRESH_RATE)
        self.beginCheckLoginCycle()

    #takes in the full database and structures the data accordingly, making the links between the separate tables
    def structure_data(self, full_data, current_data):            
        
        #make a replica of the student details as a starting point
        current_student = copy.deepcopy(current_data)
        output = {}

        #step 1: get all subjects that the student has
        subjects = []
        for subject in full_data['modules']:
            if subject['id'] in current_data['modules']:
                                
                #step 2: for each subject, get the professors that belong to that subject
                professors = []
                for prof in full_data['professors']:
                    if subject['id'] in prof['modules']:
                        
                        
                        #step 3: for each professor, get the slots that belong to that professor
                        slots = []
                        for slot in full_data['slots']:
                            if slot['prof_id'] == prof['id']:
                                slots.append(copy.deepcopy(slot))                        

                        profdata = copy.deepcopy(prof)
                        profdata['slots'] = slots
                        professors.append(profdata)
                
                subjectdata = copy.deepcopy(subject)
                subjectdata['professors'] = professors
                subjects.append(subjectdata)   
        
        output['modules'] = subjects        
        output['current'] = current_student             

        return output

if __name__ == '__main__':
    db = DBManager()
    db.InitalizeFirebase()