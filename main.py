import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label, Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SlideTransition


class MainScreen(Screen):
    pass

class NextScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")
class Main(App):

    test = 0
    def build(self):        
        # self.button = Button(text="hello") if self.test == 0 else Button(text="pressed")
        # self.button.on_press = self.change        
        return presentation

    def change(self):
        self.button.text = "test"
        print("test")


window = Main()
window.run()