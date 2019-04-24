from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle
from kivy.uix.modalview import ModalView

from ColorBoxLayout import ColorBoxLayout
from MySlotsWidget import MySlotsWidget

class StudentDetailLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self.setter('text_size'))
        self.color = (0,0,0,1)

class StudentDetailsWidget(ColorBoxLayout):
    def __init__(self, **kwargs):        
        super().__init__(color=Color(248/255,248/255,248/255,1),**kwargs)        

        self.data = {
            'name': 'nil',
            'class': 'nil',
            'student_id': 'nil'
        }

        details_container = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=200, padding=[24, 0,0, 16])        

        self.idLabel = StudentDetailLabel(text='NO ID')        
        self.nameLabel = StudentDetailLabel(text='NO NAME')                        
        self.classLabel = StudentDetailLabel(text='NO ID')        
        self.creditsLabel = StudentDetailLabel(text='NO ID')        

        details_container.add_widget(self.idLabel)
        details_container.add_widget(self.nameLabel)
        details_container.add_widget(self.classLabel)
        details_container.add_widget(self.creditsLabel)
                        
        my_slots_button = Button(text='My Slots', on_press=self.show_my_slots, size_hint=(None,None), width=160, height=80, background_normal='', background_color=(0.5,0.5,0.5,1))

        self.add_widget(details_container)
        self.add_widget(Widget())
        self.add_widget(my_slots_button)
        
        modalview = ModalView()
        self.my_slots_widget = MySlotsWidget(back_callback=self.close_modal)             
        modalview.add_widget(self.my_slots_widget)        
        self.modalview = modalview

    

    def set_student_data(self, data):                
        self.data = data
        self.nameLabel.text = 'Name: ' + data['name']                
        self.idLabel.text = 'ID: ' + data['id']                
        self.classLabel.text = 'Class: ' + data['class']                
        self.creditsLabel.text = 'Credits: {0}'.format(data['credits'])
        

    def on_size(self, *args):  
        try:
            if self._rectangle != None:
                self._rectangle.size = self.size  
                self._rectangle.pos = self.pos          
        finally:
            pass

    #filter slots and pass it to be shown
    def show_my_slots(self, instance):        
        
        #get all slots (even those that belong to me)
        dbManager = self.parent.parent.parent.dbManager
        full_data = dbManager.full_data
        
        slots = full_data['slots']
        me = full_data['current']

        my_slots = []
        for slot in slots.values():
            #if the slot belongs to me as indicated by student_id
            if slot['student_id'] == me['id']:
                my_slots.append(slot)

        
        #once i have my list of slots, i want to map the respective professor's information for display
        for slot in my_slots:            
            prof = dbManager.get_prof_with_id(slot['prof_id'])
            
            if prof != None:
                slot['prof_details'] = prof

        self.my_slots_widget.set_slots(my_slots)
        self.modalview.open()        
    
    def close_modal(self):
        self.modalview.dismiss()