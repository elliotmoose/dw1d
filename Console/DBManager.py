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

class DBManager:        
    def __init__(self):
        self.loggedIn = False
        self.data = {}
        
    def login(self, username, password):
        if username=='elliot' and password=='12345':
            return True, {'data': 'test data'}
        else:
            return False, None

    def logout(self):
        self.loggedIn = False
        self.data = {}    
        self.beginCheckLoginCycle()         