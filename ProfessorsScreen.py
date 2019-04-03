from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle

itemSpacing = 12
contentPadding = 12

from functools import partial
class ProfessorsScreen(Screen):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        #this data should be a subject
        self.subjectData = {
            'name': 'No subject selected',
            'professors' : []            
        }
        
        boxLayout = BoxLayout(orientation='vertical')
        
        #scroll view
        self.scrollView = ScrollView()
        self.contentView = BoxLayout(orientation='vertical', padding=contentPadding, spacing=itemSpacing, pos_hint={'top': 1})
        self.scrollView.add_widget(self.contentView)

        #navigation bar
        self.navigationBar = CustomBoxLayout(orientation='horizontal', size_hint_y=None, height=140)        
        
        self.backButton = Button(size_hint=(None,1), width= 260, text='< Back', background_color=(0, 0, 0, 0))
        self.backButton.on_press = self.back
                
        navBarTitles = BoxLayout(size_hint_x=None, orientation='vertical', width=800, padding=[20,0,0,8])        
        self.subjectLabel = Label(text='No subject selected', color=(0,0,0,1), size_hint_y=None, height=40, halign="left", pos_hint={'x': 0}, pos=(20, 100))
        self.subjectLabel.bind(size=self.subjectLabel.setter('text_size'))

        self.headerLabel = Label(text='Professors', size_hint_x=None, width=380, font_size=70)
        self.headerLabel.bind(size=self.headerLabel.setter('text_size'))
        navBarTitles.add_widget(self.headerLabel)
        navBarTitles.add_widget(self.subjectLabel)

        self.navigationBar.add_widget(navBarTitles)
        self.navigationBar.add_widget(Widget())
        self.navigationBar.add_widget(self.backButton)

        boxLayout.add_widget(self.navigationBar)
        boxLayout.add_widget(self.scrollView)
        self.add_widget(boxLayout)     

    def set_subject_data(self, subject):
        self.subjectData = subject
        self.subjectLabel.text = subject['name']
        self.update()

    def on_pre_enter(self, *args):                
        self.update()

    def update(self):
        self.contentView.clear_widgets()        
        buttonHeight = 200
        for i in range(len(self.subjectData['professors'])):
            
            subjectButton = Button(background_normal='', color=(0.1,0.1,0.1,1), font_size=50)
            subjectButton.size_hint_y = None 
            subjectButton.height = buttonHeight
            subjectButton.text = self.subjectData['professors'][i]['name']
            subjectButton.on_press=partial(self.select_subject, i)            
            self.contentView.add_widget(subjectButton)

        self.contentView.size_hint_y = None
        self.contentView.height = len(self.subjectData['professors'])*(buttonHeight + itemSpacing) - itemSpacing + 2*contentPadding
        
    def back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = 'SUBJECTS_SCREEN'

    def select_subject(self, index):
        self.parent.transition = SlideTransition(direction="left")
        self.parent.current = 'PROFESSORS_SCREEN'


class CustomBoxLayout(BoxLayout):  
    def __init__(self, **kwargs):  
        self.bg = InstructionGroup()   
        self.color_widget = Color(142/255, 206/255, 229/255, 1)  # red  
        self._rectangle = Rectangle()
        self.bg.add(self.color_widget)
        self.bg.add(self._rectangle)
        super(CustomBoxLayout, self).__init__(**kwargs)  
        self.canvas.add(self.bg)

    def on_size(self, *args):  
        if self._rectangle != None:
            self._rectangle.size = self.size  
            self._rectangle.pos = self.pos              