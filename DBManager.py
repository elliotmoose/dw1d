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
    def login(self, data):
        pass

    def beginCheckLoginCycle(self):
        
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

        time.sleep(0.3)
        beginCheckLoginCycle()