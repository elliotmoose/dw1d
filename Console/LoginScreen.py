from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.graphics import Color
from ColorBoxLayout import ColorBoxLayout

class LoginScreen(Screen): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = ColorBoxLayout(orientation='vertical', color=Color(1,1,1,1))
        image = Image(source='logo.png')
        
        icbs_label = Label(text="Integrated Consultation Booking System", color=(0,0,0,1),size_hint_y=None, height=120, font_size=40)                

        container.add_widget(Widget())

        container.add_widget(image)
        container.add_widget(icbs_label)        

        container.add_widget(Widget())
        
        textFieldContainer = BoxLayout(orientation='horizontal')
        boxLayout = BoxLayout(orientation='vertical', size_hint=(None,None), width=400, height=130)            
        
        #username and password text input field 
        usernameInput = TextInput(write_tab=False, size_hint_y=None, height=40)
        self.usernameInput = usernameInput
        usernameInput.hint_text = 'Username'
        passwordInput = TextInput(password=True, write_tab=False, size_hint_y=None, height=40)
        self.passwordInput = passwordInput
        passwordInput.hint_text = 'Password'
        loginButton = Button(text="Login")
        loginButton.on_press = self.login

        boxLayout.add_widget(usernameInput)
        boxLayout.add_widget(passwordInput)
        boxLayout.add_widget(loginButton)

        textFieldContainer.add_widget(Widget())
        textFieldContainer.add_widget(boxLayout)
        textFieldContainer.add_widget(Widget())

        container.add_widget(textFieldContainer)
        container.add_widget(Widget())

        self.add_widget(container)
            
    def login(self):    #function to receive username password and authenticate
        username = self.usernameInput.text
        password = self.passwordInput.text        
        success = self.parent.dbManager.login(username, password)        

        if success:     #if login is authenticated successfully, transition to the professor's slots
            self.parent.transition = SlideTransition(direction="left")
            self.parent.current = "TIMETABLE_SCREEN"                
        else:           #in case e
            print('login failed')



