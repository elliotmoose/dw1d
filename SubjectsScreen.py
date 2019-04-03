from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle

from StudentDetailsWidget import StudentDetailsWidget
from ColorBoxLayout import ColorBoxLayout

itemSpacing = 12
contentPadding = 12

from functools import partial
class SubjectsScreen(Screen):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.subjects = kwargs['subjects']
        self.data = []
        
        boxLayout = ColorBoxLayout(orientation='vertical', color=Color(162/255, 162/255, 165/255,1))
        
        #scroll view
        self.scrollView = ScrollView()
        self.contentView = BoxLayout(orientation='vertical', padding=contentPadding, spacing=itemSpacing, pos_hint={'top': 1})
        self.scrollView.add_widget(self.contentView)

        #navigation bar
        self.navigationBar = ColorBoxLayout(orientation='horizontal', size_hint_y=None, height=140)        
        
        self.backButton = Button(size_hint=(None,1), width= 260, text='< Back', background_color=(0, 0, 0, 0))
        self.backButton.on_press = self.back
                
        self.navigationBar.add_widget(Label(text='Subjects', size_hint_x=None, width=380, font_size=70))
        self.navigationBar.add_widget(Widget())
        self.navigationBar.add_widget(self.backButton)

        boxLayout.add_widget(self.navigationBar)
        boxLayout.add_widget(self.scrollView)
        self.add_widget(boxLayout)    
        
        self.studentDetailsWidget = StudentDetailsWidget(size_hint_y=None, height=200)
        self.add_widget(self.studentDetailsWidget) 

    def set_data(self, data):
        print('subject set data')
        self.data = data
        self.studentDetailsWidget.set_student_data(data['student'])        
        self.update()

    def on_pre_enter(self, *args):                
        self.update()            

    def update(self):
        self.contentView.clear_widgets()        
        buttonHeight = 200
        for i in range(len(self.data['subjects'])):
            
            subjectButton = Button(background_normal='', color=(0.1,0.1,0.1,1), font_size=50)
            subjectButton.size_hint_y = None 
            subjectButton.height = buttonHeight
            subjectButton.text = self.data['subjects'][i]['name']
            subjectButton.on_press=partial(self.select_subject, i)            
            self.contentView.add_widget(subjectButton)

        self.contentView.size_hint_y = None
        self.contentView.height = len(self.data['subjects'])*(buttonHeight + itemSpacing) - itemSpacing + 2*contentPadding
        
    def back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = 'LOGIN_SCREEN'

    def select_subject(self, index):
        self.parent.transition = SlideTransition(direction="left")
        self.parent.current = 'PROFESSORS_SCREEN'
        self.parent.professorsScreen.set_student_data(self.data['student'])
        self.parent.professorsScreen.set_subject_data(self.data['subjects'][index])

