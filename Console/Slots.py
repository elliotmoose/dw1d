
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

config = {
  "apiKey": "AIzaSyByqBZnJMeBo9CjNn111hRYWo34ipRIOwM",
  "authDomain": "basic-dc724.firebaseapp.com",
  "databaseURL": "https://basic-dc724.firebaseio.com/",
  "storageBucket": "basic-dc724.appspot.com"
}

clr3 = (1, 1, 1, 1)#for testing
green = (142/255, 229/255, 179/255, 1)#for testing
colour = (0.1, 0.1, 0.1, 1)#for testing

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class getWeek(Screen):

    def __init__(self, **kwargs):
        self.offset = 0 
        self.btn = [[None for _ in range(21)] for _ in range(21)]
        Screen.__init__(self, **kwargs)
        self.Main = GridLayout(rows = 3)
        self.add_widget(self.Main)
        self.Dayslayout = self.create_days(self.offset)
        self.Buttonlayout = self.create_buttons(self.offset)
        self.root = ScrollView()
        self.confirmButton = Button(text = 'Confirm Booking', size_hint_y=None, height=80, on_press = lambda x:self.confirmSlots())
        self.root.add_widget(self.Buttonlayout)
        self.Main.add_widget(self.Dayslayout)
        self.Main.add_widget(self.root)
        self.Main.add_widget(self.confirmButton)
        self.confirmedslots = []

    def add_offset(self):
        self.offset += 1
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

    def create_buttons(self, off):
        self.dictionary = GetWeek.getButtons(GetWeek.getWeek(off))
        ButtonLayout = GridLayout(cols=5, spacing=2, size_hint_y=None, height=21*80+22*2)
        
        for i in range(21):
            for j in range(5):
                self.btn[j][i] = ToggleButton(text=str(self.dictionary[j][i]['time'])+'\n'+str(self.dictionary[j][i]['date']),
                    group = str(self.dictionary[j][i]), 
                    state = 'normal', size_hint_y=None, 
                    height=80,text_size=(350,None),font_size='20sp', color = clr3, background_color = green)
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
        for i in range(21):
            for j in range(5):
                if(self.btn[j][i].state == 'down'):
                    self.confirmedslots.append(self.dictionary[j][i])
                    #db.child('slots').update({self.dictionary[j][i]['id']: self.dictionary[j][i]})
                    print(self.dictionary[j][i])





class ScreenApp(App):
    def build(self):
        sm = ScreenManager()
        week = getWeek(name = 'getWeek')
        sm.add_widget(week)
        return sm

ScreenApp().run()