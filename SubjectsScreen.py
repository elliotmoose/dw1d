from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import SlideTransition


class SubjectsScreen(Screen):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.subjects = kwargs['subjects']
        self.subjects = []
        
        boxLayout = BoxLayout(orientation='vertical')
        
        #scroll view
        self.scrollView = ScrollView()
        self.contentView = BoxLayout(orientation='vertical')
        self.scrollView.add_widget(self.contentView)

        #navigation bar
        self.navigationBar = BoxLayout(orientation='horizontal', size_hint_y=None, height=80)
        
        self.refreshButton = Button(size_hint=(None,1), width= 300, text='Refresh')
        self.refreshButton.on_press = self.update
        
        self.backButton = Button(size_hint=(None,1), width= 300, text='Back')
        self.backButton.on_press = self.back
        
        self.navigationBar.add_widget(self.refreshButton)
        self.navigationBar.add_widget(Widget())
        self.navigationBar.add_widget(self.backButton)

        boxLayout.add_widget(self.navigationBar)
        boxLayout.add_widget(self.scrollView)
        self.add_widget(boxLayout)     

    def on_pre_enter(self, *args):                
        self.update()

    def update(self):
        self.contentView.clear_widgets()        
        buttonHeight = 200
        for i in range(len(self.subjects)):
            subjectButton = Button()
            subjectButton.size_hint_y = None 
            subjectButton.height = buttonHeight
            subjectButton.text = self.subjects[i]
            self.contentView.add_widget(subjectButton)

        self.contentView.size_hint_y = None
        self.contentView.height = len(self.subjects)*buttonHeight
        
    def back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = 'LOGIN_SCREEN'

# class SubjectListView(BoxLayout):            
#     def __init__(self, **kwargs):                
#         super().__init__(**kwargs)
#         self.subjects = kwargs['subjects']       
#         self.orientation = 'vertical' 
#         # self.subjectListScrollView.add_widget(Button(text="test"))     
#         # self.update()       
            
#     def update(self):
#         self.contentView.clear_widgets()        
#         buttonHeight = 200
#         for i in range(len(self.subjects)):
#             subjectButton = SubjectListButton()
#             subjectButton.size_hint_y = None 
#             subjectButton.height = buttonHeight
#             subjectButton.text = subjects[i]
#             self.contentView.add_widget(subjectButton)

#         self.contentView.size_hint_y = None
#         self.contentView.height = len(subjects)*buttonHeight
#         # self.add_widget(Widget())    
            