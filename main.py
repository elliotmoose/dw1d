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
from DBManager import DBManager

    
class BookingApp(App):        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        self.screenManager = Main()   
        
    def build(self):                    
        return self.screenManager


class Main(ScreenManager):        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)                
        
        self.dbManager = DBManager(loginCallback=self.onLoggedIn)        
        
        loginScreen = LoginScreen(name="LOGIN_SCREEN")        
        self.loginScreen = loginScreen
        self.add_widget(loginScreen)

        subjectsScreen = SubjectsScreen(name="SUBJECTS_SCREEN")        
        self.subjectsScreen = subjectsScreen
        self.add_widget(subjectsScreen)

        professorsScreen = ProfessorsScreen(name="PROFESSORS_SCREEN")            
        self.professorsScreen = professorsScreen
        self.add_widget(professorsScreen)         
    
    def onLoggedIn(self, full_data):                
        self.subjectsScreen.set_data(full_data)        
        self.transition = SlideTransition(direction="left")
        self.current = "SUBJECTS_SCREEN"                


BookingApp().run()