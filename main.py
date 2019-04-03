import kivy

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.listview import ListItemButton
from kivy.uix.widget import Widget
from kivy.uix.button import Label, Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SlideTransition


from LoginScreen import LoginScreen
from SubjectsScreen import SubjectsScreen
from ProfessorsScreen import ProfessorsScreen

slot_1 = {
    'time' : '0800',
    'date' : '24/08/19'    
}

prof_1 = {
    'name' : 'Mei Xuan',
    'slots' : [
        slot_1
    ]
}

prof_2 = {
    'name' : 'Chun Kiat',
    'slots' : [
        slot_1
    ]
}

subject_1 = {
    'name' : "10.008 Engineering in the Physical World",
    'professors' : [prof_1]
}

subject_2 = {
    'name' : "10.007 Modelling the Systems World",
    'professors' : [prof_2]
}

data = {
    'subjects' : [subject_1, subject_2],
    'student' : {
        'name' : 'Elliot',
        'class' : 'F04',
        'student_id': '1003501'
    }
}        

class Main(App):        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        self.screenManager = ScreenManager()   

        loginScreen = LoginScreen(name="LOGIN_SCREEN")
        loginScreen.onLogin = self.onLogin
        self.screenManager.loginScreen = loginScreen
        self.screenManager.add_widget(loginScreen)

        subjectsScreen = SubjectsScreen(name="SUBJECTS_SCREEN")
        
        self.screenManager.subjectsScreen = subjectsScreen
        self.screenManager.add_widget(subjectsScreen)

        professorsScreen = ProfessorsScreen(name="PROFESSORS_SCREEN")        
    
        self.screenManager.professorsScreen = professorsScreen
        self.screenManager.add_widget(professorsScreen)
        

    def build(self):                    
        return self.screenManager

    def onLogin(self):
        self.screenManager.subjectsScreen.set_data(data)
        self.screenManager.transition = SlideTransition(direction="left")
        self.screenManager.current = "SUBJECTS_SCREEN"        
        print("logged in")

    

Main().run()