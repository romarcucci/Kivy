from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock

class MyPaintWidget(Widget):
    posX = 150
    posY = 150   

    goalX = 750
    goalY = 550

    def setAgent(self):
        with self.canvas:
            Color(1, 0, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(self.posX - d / 2, self.posY - d / 2), size=(d, d))
            print('Pos X: %s Pos Y: %s' %(self.posX, self.posY))

    def setGoal(self):
        with self.canvas:
            Color(0, 1, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(self.goalX - d / 2, self.goalY - d / 2), size=(d, d))
            print('Goal X: %s Goal Y: %s' %(self.goalX, self.goalY))
    
    def update(self, dt):
        with self.canvas:

            Color(0, 0, 0, mode='hsv')
            d = 30.
            Ellipse(pos=(self.posX - d / 2, self.posY - d / 2), size=(d, d))

            if self.posX < self.goalX: self.posX = self.posX+1
            if self.posX > self.goalX: self.posX = self.posX-1
            if self.posY < self.goalY: self.posY = self.posY+1
            if self.posY > self.goalY: self.posY = self.posY-1
            
            Color(1, 0, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(self.posX - d / 2, self.posY - d / 2), size=(d, d))
            print('Pos X: %s Pos Y: %s' %(self.posX, self.posY))

class MyPaintApp(App):

    def build(self):
        parent = MyPaintWidget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)
        parent.setAgent()
        parent.setGoal()
        Clock.schedule_interval(parent.update, 0.01)
        return parent

if __name__ == '__main__':
    MyPaintApp().run()