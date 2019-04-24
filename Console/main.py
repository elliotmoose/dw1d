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
from DBManager import DBManager
from TimetableScreen import TimetableScreen
    
class Main(ScreenManager):        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)                
        self.dbManager = DBManager()
        
        #INITIALIZE SCREENS
        loginScreen = LoginScreen(name="LOGIN_SCREEN")        
        self.loginScreen = loginScreen
        self.add_widget(loginScreen)

        timetableScreen = TimetableScreen(name="TIMETABLE_SCREEN")        
        self.timetableScreen = timetableScreen
        self.add_widget(timetableScreen)        

        

class ConsoleApp(App):
    def build(self):                    
        return Main()

ConsoleApp().run()