from kivy.uix.gridlayout import GridLayout
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Rectangle
#creates a grid layout class that is able to change background color
class ColorGridLayout(GridLayout):  
    def __init__(self, color=Color(142/255, 206/255, 229/255, 1),**kwargs):  
        self.bg = InstructionGroup()        
        self.color_widget = color
        self._rectangle = Rectangle()
        self.bg.add(self.color_widget)
        self.bg.add(self._rectangle)
        super(ColorGridLayout, self).__init__(**kwargs)  
        self.canvas.add(self.bg)

    def on_size(self, *args):  
        if self._rectangle != None:
            self._rectangle.size = self.size  
            self._rectangle.pos = self.pos                               