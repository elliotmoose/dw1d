from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.screenmanager import SlideTransition

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        taptologin = Button(text="Tap card to login")
        taptologin.on_press = self.nextScreen
        self.add_widget(taptologin)

    def nextScreen(self):
        self.onLogin()
        # try:
            
        # except:
        #     print('No callback defined')            

