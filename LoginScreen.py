from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.widget import Widget

from TestData import data as TESTDATA

from ColorBoxLayout import ColorBoxLayout

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = ColorBoxLayout(orientation='vertical', color=Color(1,1,1,1))
        image = Image(source='logo.png')
        
        tap_card_label = Label(text="Tap card to login", color=(0,0,0,1),size_hint_y=None, height=130)                
        icbs_label = Label(text="Integrated Consultation Booking System", color=(0,0,0,1),size_hint_y=None, height=200, font_size=70)                
        # self.add_widget(label)       

        container.add_widget(Widget())
        container.add_widget(image)
        container.add_widget(icbs_label)        
        container.add_widget(tap_card_label)
        container.add_widget(Widget())
        
        self.add_widget(container)
        
    
    def on_enter(self, *args):
        super().on_enter(*args)        
        print('Logged Out: Awaiting Login...')
        self.parent.dbManager.logout()            

    def on_leave(self, *args):
        super().on_leave(*args)

        print('login screen just left')
    

