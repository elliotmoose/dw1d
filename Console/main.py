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
# from SubjectsScreen import SubjectsScreen
# from ProfessorsScreen import ProfessorsScreen
# from DBManager import DBManager

    
class Main(App):        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        self.screenManager = ScreenManager()   
        # self.screenManager.dbManager = DBManager()
        
        loginScreen = LoginScreen(name="LOGIN_SCREEN")
        loginScreen.requestLogin = self.requestLogin
        self.screenManager.loginScreen = loginScreen
        self.screenManager.add_widget(loginScreen)

        # subjectsScreen = SubjectsScreen(name="SUBJECTS_SCREEN")
        
        # self.screenManager.subjectsScreen = subjectsScreen
        # self.screenManager.add_widget(subjectsScreen)

        # professorsScreen = ProfessorsScreen(name="PROFESSORS_SCREEN")        
    
        # self.screenManager.professorsScreen = professorsScreen
        # self.screenManager.add_widget(professorsScreen)            
                
    def build(self):                    
        return self.screenManager
    
    def requestLogin(self, username, password, callback):        
        print(username)
        print(password)

        if username=='elliot' and password=='12345':
            callback(True)

            self.screenManager.dbManager.login(data)
            self.screenManager.subjectsScreen.set_data(data)        
            self.screenManager.transition = SlideTransition(direction="left")
            self.screenManager.current = "SUBJECTS_SCREEN"        
            print("logged in")
        else:
            callback(False)

        

    

Main().run()