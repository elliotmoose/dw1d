from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.screenmanager import SlideTransition

from TestData import data as TESTDATA

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        taptologin = Button(text="Tap card to login")
        taptologin.on_press = self.nextScreen
        self.add_widget(taptologin)
    
    def on_enter(self, *args):
        super().on_enter(*args)

        print('Logged Out: Awaiting Login...')
        self.parent.dbManager.logout()

    def nextScreen(self):
        self.parent.dbManager.login(TESTDATA)

