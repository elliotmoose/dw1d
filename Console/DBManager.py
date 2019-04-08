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
        pass

    def logout(self):
        self.loggedIn = False
        self.data = {}    
        self.beginCheckLoginCycle()         