from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
   
startPosX = 150
startPosY = 150

goalX = 750
goalY = 550

class MyPaintWidget(Widget):

    def setAgent(self):
        with self.canvas:
            Color(1, 0, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(startPosX - d / 2, startPosY - d / 2), size=(d, d))
            print('Pos X: %s Pos Y: %s' %(startPosX, startPosY))

    def setGoal(self):
        with self.canvas:
            Color(0, 1, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(goalX - d / 2, goalY - d / 2), size=(d, d))
            print('Goal X: %s Goal Y: %s' %(goalX, goalY))

class MyPaintApp(App):

    def build(self):
        parent = MyPaintWidget()
        self.painter = MyPaintWidget()
        startBtn = Button(text='Start')
        startBtn.bind(on_release=self.start_exp)
        parent.add_widget(self.painter)
        parent.add_widget(startBtn)
        parent.setAgent()
        parent.setGoal()
        return parent

    def start_exp(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()