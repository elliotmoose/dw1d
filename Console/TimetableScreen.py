from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color

#asdaklfjlskdj
#shankai was not here
#elliot was here

from ColorBoxLayout import ColorBoxLayout

class TimetableScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_data(self, data):
        self.data = data

    
    
