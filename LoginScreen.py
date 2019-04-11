from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import SlideTransition

from TestData import data as TESTDATA

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = Label(text="Tap card to login")                
        self.add_widget(label)       
        
    
    def on_enter(self, *args):
        super().on_enter(*args)        
        print('Logged Out: Awaiting Login...')
        self.parent.dbManager.logout()            

    def on_leave(self, *args):
        super().on_leave(*args)

        print('login screen just left')
    

