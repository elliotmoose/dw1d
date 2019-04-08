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
    def __init__(self):
        self.loggedIn = False
        self.data = {}        
        
        #connect
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()                
    
    def InitalizeFirebase(self):

        confirmed = input('Warning: Initializing removes all current data. Continue? y/n\n')
        
        if confirmed != 'y':
            return

        print('Initializing database...')
        
        self.db.update(TestData.dbtemplate)
        
        print('Initializing done!')

    def login(self, data):
        self.loggedIn = True
        self.data = data

        print('USER LOGGED IN WITH DATA:')
        print(data)

    def logout(self):
        self.loggedIn = False
        self.data = {}    
        self.beginCheckLoginCycle() 
           
    def beginCheckLoginCycle(self):
        t = Timer(0.1, self._beginCheckLoginCycle)
        t.start()        
        #read from firebase
        #if firebase has a current user
        #get data = {
        #   subjects : [
        #       {
        #           title: '',
        #
        #       }
        #   ],
        #   user : {
        #       name : '',
        #       student_id: 1009999,
        #       class : 'F04'  
        #   }
        # }
        #call self.login(data)        
        
    #this is an internal function because it has to be run with a timer (so that it is multithreaded)
    def _beginCheckLoginCycle(self):
        
        if self.loggedIn:
            return

        print('Reading from firebase..')
        time.sleep(1)
        self.beginCheckLoginCycle()


if __name__ == '__main__':
    db = DBManager()
    db.InitalizeFirebase()