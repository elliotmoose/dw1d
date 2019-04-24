"""

    DBMANAGER HANDLES ALL INTERACTION WITH DATABASE

    - Connection
    - Receiving Login
    - Loading of data (e.g. Loading available slots)
    - Updating of data (e.g. Confirming of slots)
    - Structuring of data

    FOR TESTING PURPOSES:
    
    Running the following command simulates a login:
    
    $ python3 DBManager.py login

    Running the following command will prompt user to re-populate database:

    $ python3 DBManager.py

"""

import time
from threading import Timer
from libdw import pyrebase
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
        self.structured_data = {}        
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

    #For testing purposes, this function lets you simulate the tapping of a card and login
    def FirebaseForceLogin(self):
        current = self.db.child('students/{0}'.format('1003501')).get().val()
        self.db.update({'current': current})

    def login(self, structured_data):
        self.loggedIn = True
        self.structured_data = structured_data

        print('USER LOGGED IN')        

        if self.loginCallback != None:
            self.loginCallback(structured_data)

    def logout(self):
        self.db.child('current').remove()
        self.loggedIn = False
        self.structured_data = {}    
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
            self.full_data = full_db
            self.login(structured_data)
            return

        #call itself to keep checking database
        time.sleep(1/REFRESH_RATE)
        self.beginCheckLoginCycle()

    #retrieves all data again, structures it, then returns it
    def reloadStructuredData(self):
        
        print('Reloading all data...')
        current = self.db.child('current').get().val()

        if current != None:            
            full_db = self.db.get().val()
            self.structured_data = self.structure_data(full_db, current)
            self.full_data = full_db                        
            return self.structured_data
        else:
            print('ERROR: NO CURRENT USER')
            return None

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
                        for slot in full_data['slots'].values():
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

    #confirm the slot by updating firebase and allocating the currently logged in student's id as the student of the slot
    #returns the slot that was confirmed
    def confirm_slot(self, slot_uuid):
        print('Confirming Slot...')    
        allslots = self.full_data['slots']
        student = self.full_data['current']        
        student_id = student['id']
        
        price = 50
        newcredits = student['credits'] - price     

        if newcredits < 0:   
            return None
        
        print('new credits: ', newcredits)    

        #update database with student_id, signifying the slot has been booked, and allocating the new credits amount
        self.db.update({
            'slots/{0}/student_id'.format(slot_uuid): student_id,
            'students/{0}/credits'.format(student_id) : newcredits,
            'current/credits' : newcredits
        })        

        return self.db.child('slots/{0}'.format(slot_uuid)).get().val()

    def get_student(self):
        return self.structure_data['current']

    def get_prof_with_id(self, id):        
        for prof in self.full_data['professors']:
            if prof['id'] == id:
                return prof


        
                
                
import sys
if __name__ == '__main__':
    db = DBManager()

    if len(sys.argv) > 1 and sys.argv[1] == 'login':
        db.FirebaseForceLogin()
    else:    
        db.InitalizeFirebase()    

