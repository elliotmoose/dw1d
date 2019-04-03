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
class ProfessorsScreen(Screen):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        #this data should be a subject
        self.subjectData = {
            'name': 'No subject selected',
            'professors' : []            
        }
        
        boxLayout = ColorBoxLayout(orientation='vertical', color=Color(162/255, 162/255, 165/255,1))
        
        bodyContainer = BoxLayout(orientation='horizontal')                

        #navigation bar ==
        self.navigationBar = ColorBoxLayout(orientation='horizontal', size_hint_y=None, height=140)        
        
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
        #end == 


        #profs
        self.scrollView = ScrollView()
        self.contentView = BoxLayout(orientation='vertical', padding=contentPadding, spacing=itemSpacing, pos_hint={'top': 1})
        self.scrollView.add_widget(self.contentView)

        #slots
        self.slotsView = SlotsWidget(orientation='vertical', color=Color(228/255,228/255,228/255,1))        

        #prof detail        
        self.profDetailsView = ProfDetailsWidget(orientation='vertical', color=Color(248/255,248/255,248/255,1))

        bodyContainer.add_widget(self.scrollView) 
        bodyContainer.add_widget(self.slotsView)
        bodyContainer.add_widget(self.profDetailsView)

        boxLayout.add_widget(self.navigationBar)
        boxLayout.add_widget(bodyContainer)       

        self.add_widget(boxLayout)     
        
        self.studentDetailsWidget = StudentDetailsWidget(size_hint_y=None, height=200)
        self.add_widget(self.studentDetailsWidget) 

    def set_subject_data(self, subject):
        self.subjectData = subject
        self.subjectLabel.text = subject['name']
        self.update()

    def set_student_data(self, student_data):
        self.student_data = student_data
        self.studentDetailsWidget.set_student_data(student_data)        

    def on_pre_enter(self, *args):                
        self.update()

    def on_leave(self, *args):
        self.profDetailsView.reset_prof_data()
        print('leaving')

    def update(self):
        self.contentView.clear_widgets()        
        buttonHeight = 200
        for i in range(len(self.get_profs())):            
            profButton = Button(background_normal='', color=(0.1,0.1,0.1,1), font_size=50)
            profButton.size_hint_y = None 
            profButton.height = buttonHeight
            profButton.text = self.get_prof_at_index(i)['name']
            profButton.on_press=partial(self.select_prof, i)            
            self.contentView.add_widget(profButton)

        self.contentView.size_hint_y = None
        self.contentView.height = len(self.subjectData['professors'])*(buttonHeight + itemSpacing) - itemSpacing + 2*contentPadding
        
    def back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = 'SUBJECTS_SCREEN'

    def select_prof(self, index):
        # self.parent.transition = SlideTransition(direction="left")
        # self.parent.current = 'SLOTS_SCREEN'
        # self.parent.slotsScreen.set_student_data(self.student_data)
        # self.parent.slotsScreen.set_subject_data(self.subjectData)
        # self.parent.slotsScreen.set_prof_data(self.get_prof(index))        
        self.profDetailsView.set_prof_data(self.get_prof_at_index(index))

    def get_profs(self):
        return self.subjectData['professors']

    def get_prof_at_index(self, index):
        return self.subjectData['professors'][index]


class SlotsWidget(ColorBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfDetailsWidget(ColorBoxLayout):   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        

        self.padding = [24,18,0,0]

        self.headerLabel = ProfDetailLabel(text='Professor Details:')
        self.add_widget(self.headerLabel)

        self.profNameLabel = ProfDetailLabel(text='Name: ')
        self.add_widget(self.profNameLabel)
        
        self.profEmailLabel = ProfDetailLabel(text='Email: ')
        self.add_widget(self.profEmailLabel)
        
        self.profContactLabel = ProfDetailLabel(text='Contact: ')
        self.add_widget(self.profContactLabel)        

        self.add_widget(Widget())

        self.reset_prof_data()

    def set_prof_data(self, prof_data):
        self.prof_data = prof_data
        self.update()        

    def reset_prof_data(self):
        self.prof_data = None

        self.update()

    def update(self):
        if self.prof_data == None:
            self.profNameLabel.text = 'No Selection'
            self.profEmailLabel.text = ''
            self.profContactLabel.text = ''
        else:    
            self.profNameLabel.text = 'Name: ' + self.prof_data['name']
            self.profEmailLabel.text = 'Email: ' + self.prof_data['email']
            self.profContactLabel.text = 'Contact: ' + self.prof_data['contact']
        


class ProfDetailLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self.setter('text_size'))
        self.color = (0,0,0,1)
        self.size_hint_y = None
        self.height = 40
