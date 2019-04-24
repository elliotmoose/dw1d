from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from ColorBoxLayout import ColorBoxLayout
from NavigationBar import NavigationBar
from kivy.graphics import Color

from DateHelper import DateTimeStringToEpoch

import copy

textColor = (0.1,0.1,0.1,1)
class MySlotsWidget(ColorBoxLayout):
    def __init__(self, back_callback, **kwargs):
        super().__init__(**kwargs)
        
        # self.add_widget(NavigationBar('My Slots','', back_callback))        
        self.container = ColorBoxLayout(orientation='vertical')

        #Bottom Navigation Bar
        self.bottomNavigationBar = ColorBoxLayout(orientation='horizontal', size_hint_y=None, height=140)
        self.backButton = Button(size_hint=(None,1), width= 260, text='< Back', background_color=(0, 0, 0, 0))
        self.backButton.on_press = back_callback
                    
        self.headerLabel = Label(text='My Slots', size_hint=(None,None),height=140, width=380, font_size=70)
        self.headerLabel.bind(size=self.headerLabel.setter('text_size'))
        self.bottomNavigationBar.add_widget(self.headerLabel)        
        self.bottomNavigationBar.add_widget(Widget())
        self.bottomNavigationBar.add_widget(self.backButton)
        #end =====


        #Slots Display
        self.scrollview = ScrollView()
        self.slots_container = ColorBoxLayout(orientation='vertical')



        self.scrollview.add_widget(self.slots_container)                
        
        self.container.add_widget(self.scrollview)
        self.container.add_widget(Widget())
        self.container.add_widget(self.bottomNavigationBar)

        self.add_widget(self.container)

    def set_slots(self, input_slots):        
        
        slots = copy.copy(input_slots)
        slots.sort(key=lambda x: DateTimeStringToEpoch(x['date']+' '+x['time']))
        

        self.slots_container.clear_widgets()
        
        for slot in slots:
            slot_item = ColorBoxLayout(orientation='horizontal', size_hint_y=None, height=60, color=Color(1,1,1,1))

            timeLabel = Label(text=slot['time'],color=textColor, size_hint_x=None, width = 180)
            dateLabel = Label(text=slot['date'],color=textColor, size_hint_x=None, width = 150)
            profNameLabel = Label(text=slot['prof_details']['name'],color=textColor)
            profContactLabel = Label(text=slot['prof_details']['contact'],color=textColor)
            profEmailLabel = Label(text=slot['prof_details']['email'],color=textColor)

            slot_item.add_widget(timeLabel)
            slot_item.add_widget(dateLabel)
            slot_item.add_widget(profNameLabel)
            slot_item.add_widget(profContactLabel)
            slot_item.add_widget(profEmailLabel)

            self.slots_container.add_widget(slot_item)

            

    