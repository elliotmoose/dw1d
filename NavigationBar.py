from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from ColorBoxLayout import ColorBoxLayout

navigationBarHeight = 140

class NavigationBar(ColorBoxLayout):    
    def __init__(self, title, subtitle,back_callback, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=navigationBarHeight, **kwargs)                        
        
        self.backButton = Button(size_hint=(None,1), width= 260, text='< Back', background_color=(0, 0, 0, 0))
        self.backButton.on_press = back_callback
                
        navBarTitles = BoxLayout(size_hint_x=None, orientation='vertical', width=800, padding=[20,0,0,8])        
        self.subtitleLabel = Label(text=subtitle, color=(0,0,0,1), size_hint_y=None, height=40, halign="left", pos_hint={'x': 0}, pos=(20, 100))
        self.subtitleLabel.bind(size=self.subtitleLabel.setter('text_size'))

        self.headerLabel = Label(text=title, size_hint_x=None, width=380, font_size=70)
        self.headerLabel.bind(size=self.headerLabel.setter('text_size'))
        navBarTitles.add_widget(self.headerLabel)
        navBarTitles.add_widget(self.subtitleLabel)

        self.add_widget(navBarTitles)
        self.add_widget(Widget())
        self.add_widget(self.backButton)        
