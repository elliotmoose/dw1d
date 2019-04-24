import GetWeek
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import ButtonBehavior
import uuid
from kivy.uix.popup import Popup
from functools import partial
from ColorGridLayout import ColorGridLayout
from kivy.graphics import Color
from kivy.uix.screenmanager import SlideTransition

#Colours for the slots
BLACK = (0.1, 0.1, 0.1, 1)
YELLOW = (255/255,242/255,127/255,1)
BLUE = (114/255, 182/255, 216/255, 1)
GREEN = (142/255, 229/255, 179/255, 1)

class TimetableScreen(Screen):

    def __init__(self, **kwargs):
        self.offset = 0     #offset is to generate the next/previous week's weekly schedules
        self.btn = [[None for _ in range(21)] for _ in range(21)]       #initialize empty variables to be used by button slots
        Screen.__init__(self, **kwargs)
        self.Main = GridLayout(rows = 3)    
        self.add_widget(self.Main)
        self.Dayslayout = self.create_days(self.offset)
        self.Buttonlayout = GridLayout()        #initialize the base gridlayout for the timetable screen
        self.root = ScrollView()                #to implement scroll view for the slots
        self.root.add_widget(self.Buttonlayout) #adding subsequent widgets to the scroll and grid layouts
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)

    def on_enter(self): 
        self.update()

    def add_offset(self): #to add offset when user navigates to the next week
        self.offset += 1
        self.update()
        

    def update(self):   #to rebuild the screen widgets
        self.Main.clear_widgets()
        self.Buttonlayout.clear_widgets()
        self.Buttonlayout = self.create_buttons(self.offset)
        self.root.clear_widgets()
        self.root.add_widget(self.Buttonlayout)
        self.Dayslayout.clear_widgets()
        self.Dayslayout = self.create_days(self.offset)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)

    def dec_offset(self): #to decrease offset when user navigates to previous week
        self.offset -= 1
        self.update()

                                
    def is_in_db(self, i, j):   #checks if the slot at index, i,j exists in the database    
        my_prof_slots = self.parent.dbManager.my_prof_slots
        slot_to_check = self.dictionary[j][i]

        for slot in my_prof_slots:
            if slot['time'] == slot_to_check['time'] and slot['date'] == slot_to_check['date']:
                return True

        return False

    def is_booked(self, i, j):  #checks if a student has booked the available slot
        try:
            return self.dictionary[j][i]['student_id'] != 'null'
        except:
            return False

    def create_buttons(self, off): #to create the slot buttons which are representative of the dictionary of slots
        self.dictionary = GetWeek.getSlots(GetWeek.getWeek(off), self.parent.dbManager.my_prof['id'])
        for i in range(21):
            for j in range(5):
                for db_slot in self.parent.dbManager.my_prof_slots:
                    local_slot = self.dictionary[j][i]
                    if local_slot['date'] == db_slot['date'] and local_slot['time'] == db_slot['time']:  
                        self.dictionary[j][i] = db_slot
        
        ButtonLayout = GridLayout(cols=5, spacing=2, size_hint_y=None, height=21*80+22*2)
        
        for i in range(21):
            for j in range(5):
                if self.is_in_db(i,j):
                    if self.is_booked(i,j):
                        colorvar = GREEN    #sets the slot colour to green if a student has booked it
                    else:
                        colorvar = YELLOW   #sets the slot colour to yellow if the professor has declared his availability but is unbooked by students
                else:
                    colorvar = BLUE         #sets default colour to blue to represent lack of availability
                self.btn[j][i] = Button(text=str(self.dictionary[j][i]['time'])+'\n'+str(self.dictionary[j][i]['date']), 
                    size_hint_y=None, 
                    height=80, font_size = 18, 
                    halign='center', color = BLACK, 
                    background_color = colorvar,
                    on_release = partial(self.select_slot, i, j), 
                    background_normal = '')
                ButtonLayout.add_widget(self.btn[j][i])
        
        return ButtonLayout
    
    def create_days(self, off): #to create day labels to signify the days of the week
        DaysLayout = ColorGridLayout(cols = 5, spacing = 2, size_hint_y=None, width=160, color = Color(0.2,0.2,0.2,1)) 
        mon = Label(text = 'Monday', font_size = 24)
        tue = Label(text = 'Tuesday', font_size = 24)
        wed = Label(text = 'Wednesday', font_size = 24)
        thu = Label(text = 'Thursday', font_size = 24)
        fri = Label(text = 'Friday', font_size = 24)
        days = [mon, tue, wed, thu, fri]
        nextweek = Button(text = 'Next Week', on_press = lambda x:self.add_offset())
        prevweek = Button(text = 'Previous Week', on_press = lambda x:self.dec_offset())
        refresh = Button(text = "Refresh", on_press = lambda x:self.refresh())
        logout = Button(text = 'Logout', on_press = lambda x:self.logout())
        legend = Button(text = 'Legend', on_press = lambda x:self.legend())
        DaysLayout.add_widget(legend)
        DaysLayout.add_widget(prevweek)     
        DaysLayout.add_widget(refresh)
        DaysLayout.add_widget(nextweek)
        DaysLayout.add_widget(logout)
        for day in days:
            DaysLayout.add_widget(day)
        return DaysLayout

    def select_slot(self, i, j, x): #if any slot is clicked, this function is called
        if self.is_booked(i, j):    #if the slot is booked by a student
            current = self.dictionary[j][i] 
            student_id = current['student_id']
            student_details = self.parent.dbManager.full_db['students'][student_id]
            popup = Popup(title = 'Booking Details',
                          content = Label(text = 'Time: {}\nDate: {}\nStudent ID: {}\nName: {}\nEmail: {}\nClass: {}'.format(current['time'], 
                              current['date'], 
                              current['student_id'], 
                              student_details['name'], 
                              student_details['email'], 
                              student_details['class']), font_size = 20),
                          size_hint = (None, None),
                          size = (350, 250))
            popup.open()
            #pop up containing the student details who booked the selected slot         
        
        elif self.is_in_db(i, j):#if a previously declared available slot is clicked, it undoes the confirmation and removes that slot from the database
            self.parent.dbManager.removeDBSlots(self.dictionary[j][i])
                
        else:       #if an empty slot is clicked, it is pushed to database with an UUID as the key for the slot
            self.dictionary[j][i]['id'] = str(uuid.uuid4())
            self.parent.dbManager.updateDBSlots(self.dictionary[j][i])
        self.update()
    
    def legend(self):   #func to display a legend to display the differently coloured slots
        LegendLayout = GridLayout(rows = 2)
        picture = Button(background_normal = 'legend.jpg')
        closepopup = Button(text = 'Close', size_hint_y = (None),
                          size = (50, 50))
        LegendLayout.add_widget(picture)
        LegendLayout.add_widget(closepopup)
        popup = Popup(title = 'Legend', content = LegendLayout, auto_dismiss=False,
                        size_hint = (None, None),
                          size = (350, 400))
        closepopup.bind(on_press=popup.dismiss)
        popup.open()
    
    def refresh(self):  #to refresh the slots to check for updates in the slot bookings
        self.parent.dbManager.reloadSlots()
        self.update()
        

    def logout(self):   #to allow the professor to log out and transit back to login screen
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = "LOGIN_SCREEN" 

 



