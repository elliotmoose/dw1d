from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from ColorBoxLayout import ColorBoxLayout
from NavigationBar import NavigationBar

class MySlotsWidget(ColorBoxLayout):
    def __init__(self, back_callback, **kwargs):
        super().__init__(**kwargs)
        
        # self.add_widget(NavigationBar('My Slots','', back_callback))        

        self.slots_container = ColorBoxLayout(orientation='vertical')

        self.add_widget(self.slots_container)        

    def set_slots(self, slots):        
        print(slots)

    