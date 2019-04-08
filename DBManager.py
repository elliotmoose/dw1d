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

FIREBASE_ENDPOINT = 'https://basic-dc724.firebaseio.com/'
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
        t = Timer(0.1, self._beginCheckLoginCycle)
        t.start()        
 
    #this is an internal function because it has to be run with a timer (so that it is multithreaded)
    def _beginCheckLoginCycle(self):
        
        #if it is logged in, no more need to check
        if self.loggedIn:
            return

        print('Reading from firebase..')

        #get current student (logged in)
        current = self.db.child('current').get().val()
        if current != None:            
            full_db = self.db.get().val()
            self.login(self.structure_data(full_db))
            return

        #call itself to keep checking database
        time.sleep(1)
        self.beginCheckLoginCycle()

    #takes in the full database and structures the data accordingly, making the links between the separate tables
    def structure_data(self, unprocessed_data):            
        return unprocessed_data

if __name__ == '__main__':
    db = DBManager()
    db.InitalizeFirebase()