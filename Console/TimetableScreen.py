
import GetWeek
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from libdw import pyrebase
from kivy.uix.button import ButtonBehavior
import uuid
from functools import partial

config = {
  "apiKey": "AIzaSyByqBZnJMeBo9CjNn111hRYWo34ipRIOwM",
  "authDomain": "basic-dc724.firebaseapp.com",
  "databaseURL": "https://basic-dc724.firebaseio.com/",
  "storageBucket": "basic-dc724.appspot.com"
}

clr3 = (1, 1, 1, 1)#for testing
colour = (0.1, 0.1, 0.1, 1)#for testing
RED = (229/255,142/255,142/255,1)
BLUE = (114/255, 182/255, 216/255, 1)
GREEN = (142/255, 229/255, 179/255, 1)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

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
        self.confirmButton = Button(text = 'Confirm Availability', size_hint_y=None, height=80, on_press = lambda x:self.confirmSlots())
        self.root.add_widget(self.Buttonlayout)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)
        self.Main.add_widget(self.confirmButton)
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
        self.Main.add_widget(self.confirmButton)

    def dec_offset(self):
        self.offset -= 1
        self.Main.clear_widgets()
        self.Buttonlayout.clear_widgets()
        self.Buttonlayout = self.create_buttons(self.offset)
        self.root.clear_widgets()
        self.root.add_widget(self.Buttonlayout)
        self.Dayslayout.clear_widgets()
        self.Dayslayout = self.create_days(self.offset)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)
        self.Main.add_widget(self.confirmButton)

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
        self.dictionary = GetWeek.getButtons(GetWeek.getWeek(off))
        ButtonLayout = GridLayout(cols=5, spacing=2, size_hint_y=None, height=21*80+22*2)

        # slotlist = []
        # for item in list(db.child('slots').get().val()):
        #     slotlist.append(db.child('slots').get().val()[item]['date']+db.child('slots').get().val()[item]['time'])

        for i in range(21):
            for j in range(5):
                if self.is_in_db(i,j):
                    if self.is_booked(i,j):
                        colorvar = RED
                    else:
                        colorvar = GREEN
                else:
                    colorvar = BLUE
                self.btn[j][i] = Button(text=str(self.dictionary[j][i]['time'])+'\n'+str(self.dictionary[j][i]['date']), 
                    size_hint_y=None, 
                    height=80,text_size=(350,None),font_size='20sp', color = clr3, background_color = colorvar,
                    on_release = partial(self.select_slot, i, j), background_normal = '')
                ButtonLayout.add_widget(self.btn[j][i])
        
        return ButtonLayout
    
    def create_days(self, off):
        DaysLayout = GridLayout(cols = 5, spacing = 2, size_hint_y=None, width=160) 
        mon = Label(text = 'Monday', font_size = 24)
        tue = Label(text = 'Tuesday', font_size = 24)
        wed = Label(text = 'Wednesday', font_size = 24)
        thu = Label(text = 'Thursday', font_size = 24)
        fri = Label(text = 'Friday', font_size = 24)
        days = [mon, tue, wed, thu, fri]
        nextweek = Button(text = 'Next Week', on_press = lambda x:self.add_offset(), color = colour, background_color = (1,1,1,1), background_normal = '')
        prevweek = Button(text = 'Previous Week', on_press = lambda x:self.dec_offset())
        #only the 2nd offset onwards have prevweek
        if off != 0:
            DaysLayout.add_widget(prevweek)
        else:
            DaysLayout.add_widget(Label(text = ''))

        for i in range(3):    
            DaysLayout.add_widget(Label(text = ''))
        DaysLayout.add_widget(nextweek)

        for day in days:
            DaysLayout.add_widget(day)
        return DaysLayout

    def confirmSlots(self):
        self.parent.dbManager.updateDbSlots(self.tempAvailSlots)
        # for i in range(21):
        #     for j in range(5):
        #         # append available selected slots to a temporary list and then push to db together
        #         # if(self.btn[j][i].background_color == GREEN):
        #         #     self.confirmedslots.append(self.dictionary[j][i])
        #         #     db.child('slots').update({self.dictionary[j][i]['id']: self.dictionary[j][i]})
        #             #print(self.dictionary[j][i])

    def select_slot(self, i, j, x):
        print('slot selected')
        if self.is_in_db(i, j):
            #delete
            pass
        elif self.is_booked(i, j):
            #show modal with student info
            pass
        else:
            print('reached here')
            self.tempAvailSlots = []
            self.tempAvailSlots.append(self.dictionary[j][i])
        self.update()

    def createUUID(self, data):
        

    




# class ScreenApp(App):
#     def build(self):
#         sm = ScreenManager()
#         week = getWeek(name = 'getWeek')
#         sm.add_widget(week)
#         return sm

# ScreenApp().run()



