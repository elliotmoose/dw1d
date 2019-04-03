from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle

from ColorBoxLayout import ColorBoxLayout

class StudentDetailLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self.setter('text_size'))
        self.color = (0,0,0,1)

class StudentDetailsWidget(Widget):
    def __init__(self, **kwargs):
        
        self.bg = InstructionGroup()   
        self.color_widget = Color(248/255,248/255,248/255,1) 
        self._rectangle = Rectangle()
        self.bg.add(self.color_widget)
        self.bg.add(self._rectangle)
        super().__init__(**kwargs)
        self.canvas.add(self.bg)

        self.data = {
            'name': 'nil',
            'class': 'nil',
            'student_id': 'nil'
        }

        container = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=200, padding=[24, 0,0, 16])        

        self.nameLabel = StudentDetailLabel(text='NO NAME')                        
        self.idLabel = StudentDetailLabel(text='NO ID')        
        self.classLabel = StudentDetailLabel(text='NO ID')        

        container.add_widget(self.nameLabel)
        container.add_widget(self.idLabel)
        container.add_widget(self.classLabel)
                
        self.add_widget(container)
        self.add_widget(Widget())
        

        

    def set_student_data(self, data):        
        print(self.data)
        self.data = data
        self.nameLabel.text = 'Name: ' + data['name']                
        self.idLabel.text = 'ID: ' + data['student_id']                
        self.classLabel.text = 'Class: ' + data['class']                
        

    def on_size(self, *args):  
        try:
            if self._rectangle != None:
                self._rectangle.size = self.size  
                self._rectangle.pos = self.pos          
        finally:
            print("no rect")    