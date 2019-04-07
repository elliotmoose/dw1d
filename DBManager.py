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


class DBManager:        
    def __init__(self):
        self.loggedIn = False
        self.data = {}
        
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