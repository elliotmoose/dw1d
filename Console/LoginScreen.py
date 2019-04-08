from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.graphics import Color

from ColorBoxLayout import ColorBoxLayout

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = AnchorLayout(anchor_x='center', anchor_y='center')
        boxLayout = ColorBoxLayout(orientation='vertical', size_hint=(None,None), width=400, height=200, color=Color(0,0,0,1))            

        usernameInput = TextInput(write_tab=False)
        self.usernameInput = usernameInput
        usernameInput.hint_text = 'Username'
        passwordInput = TextInput(password=True, write_tab=False)
        self.passwordInput = passwordInput
        passwordInput.hint_text = 'Password'
        taptologin = Button(text="Login")
        taptologin.on_press = self.login

        boxLayout.add_widget(usernameInput)
        boxLayout.add_widget(passwordInput)
        boxLayout.add_widget(taptologin)

        container.add_widget(boxLayout)
        self.add_widget(container)
    
    def on_enter(self, *args):
        super().on_enter(*args)

        print('Logged Out: Awaiting Login...')
        # self.parent.dbManager.logout()

    # def beginCheckLogin(self):        
    #     data = self.parent.dbManager.beginCheckLoginCycle() #this function 
    #     self.loginCallback(data)                

    def login(self):
        username = self.usernameInput.text
        password = self.passwordInput.text
        self.requestLogin(username, password, self.loginCallback)        

    def loginCallback(self, success):
        print(success)

