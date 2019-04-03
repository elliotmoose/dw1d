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

subjects = ["10.008 Engineering in the Physical World", "3.007 Introduction to Design","3","4","5","6","7","8"]        

class Main(App):        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        self.screenManager = ScreenManager()   
        self.screenManager.add_widget(LoginScreen(name="LOGIN_SCREEN"))
        subjectsScreen = SubjectsScreen( name="SUBJECTS_SCREEN")
        subjectsScreen.subjects = subjects
        self.screenManager.add_widget(subjectsScreen)        

    def build(self):                    
        return self.screenManager

    def change(self):
        self.button.text = "test"
        print("test")

Main().run()