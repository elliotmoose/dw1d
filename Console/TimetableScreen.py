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

BLACK = (0.1, 0.1, 0.1, 1)
YELLOW = (255/255,242/255,127/255,1)
BLUE = (114/255, 182/255, 216/255, 1)
GREEN = (142/255, 229/255, 179/255, 1)

class TimetableScreen(Screen):

    def __init__(self, **kwargs):
        self.offset = 0 
        self.btn = [[None for _ in range(21)] for _ in range(21)]
        Screen.__init__(self, **kwargs)
        self.Main = GridLayout(rows = 3)
        self.add_widget(self.Main)
        self.Dayslayout = self.create_days(self.offset)
        # self.Buttonlayout = self.create_buttons(self.offset)
        self.Buttonlayout = GridLayout()
        self.root = ScrollView()
        #self.confirmButton = Button(text = 'Confirm Availability', size_hint_y=None, height=80, on_press = lambda x:self.confirmSlots())
        self.root.add_widget(self.Buttonlayout)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)
        #self.Main.add_widget(self.confirmButton)
        self.confirmedslots = []

    def on_enter(self):
        self.update()

    def add_offset(self):
        self.offset += 1
        self.update()
        

    def update(self):
        self.Main.clear_widgets()
        self.Buttonlayout.clear_widgets()
        self.Buttonlayout = self.create_buttons(self.offset)
        self.root.clear_widgets()
        self.root.add_widget(self.Buttonlayout)
        self.Dayslayout.clear_widgets()
        self.Dayslayout = self.create_days(self.offset)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)
        # self.Main.add_widget(self.confirmButton)

    def dec_offset(self):
        self.offset -= 1
        self.update()

    #checks if the slot at index, i,j has been created in the database
    def is_in_db(self, i, j):    

        my_prof_slots = self.parent.dbManager.my_prof_slots

        slot_to_check = self.dictionary[j][i]

        for slot in my_prof_slots:
            if slot['time'] == slot_to_check['time'] and slot['date'] == slot_to_check['date']:
                return True

        return False

    def is_booked(self, i, j):
        try:
            return self.dictionary[j][i]['student_id'] != 'null'
        except:
            return False



    def create_buttons(self, off):
        self.dictionary = GetWeek.getButtons(GetWeek.getWeek(off), self.parent.dbManager.my_prof['id'])

        for i in range(21):
            for j in range(5):
                for db_slot in self.parent.dbManager.my_prof_slots:
                    local_slot = self.dictionary[j][i]
                    
                    if local_slot['date'] == db_slot['date'] and local_slot['time'] == db_slot['time']:  
                        self.dictionary[j][i] = db_slot


        ButtonLayout = GridLayout(cols=5, spacing=2, size_hint_y=None, height=21*80+22*2)

        # slotlist = []
        # for item in list(db.child('slots').get().val()):
        #     slotlist.append(db.child('slots').get().val()[item]['date']+db.child('slots').get().val()[item]['time'])

        for i in range(21):
            for j in range(5):
                if self.is_in_db(i,j):
                    if self.is_booked(i,j):
                        colorvar = GREEN
                    else:
                        colorvar = YELLOW
                else:
                    colorvar = BLUE
                self.btn[j][i] = Button(text=str(self.dictionary[j][i]['time'])+'\n'+str(self.dictionary[j][i]['date']), 
                    size_hint_y=None, 
                    height=80, font_size = 18, halign='center', color = BLACK, background_color = colorvar,
                    on_release = partial(self.select_slot, i, j), background_normal = '')
                ButtonLayout.add_widget(self.btn[j][i])
        
        return ButtonLayout
    
    def create_days(self, off): 
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
        
        #insert buttons
        DaysLayout.add_widget(legend)
        #only the 2nd offset onwards have prevweek
        DaysLayout.add_widget(prevweek)     
        DaysLayout.add_widget(refresh)
        DaysLayout.add_widget(nextweek)
        DaysLayout.add_widget(logout)
        for day in days:
            DaysLayout.add_widget(day)
        return DaysLayout

    def select_slot(self, i, j, x):        
        #has to check if it is booked first, otherwise is_in_db will clear first
        if self.is_booked(i, j):
            print('popup triggered')
            current = self.dictionary[j][i] #checks db for booked slots
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
            #show modal with student info
        
        elif self.is_in_db(i, j):
            print('removing slots')
            self.parent.dbManager.removeDBSlots(self.dictionary[j][i])
                
        else:
            print('reached here')
            self.dictionary[j][i]['id'] = str(uuid.uuid4())
            self.parent.dbManager.updateDBSlots(self.dictionary[j][i])
            
        self.update()
    
    def legend(self):
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
    
    def refresh(self):
        print('reached refresh')
        self.parent.dbManager.reloadSlots()
        self.update()
        

    def logout(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = "LOGIN_SCREEN" 

 



