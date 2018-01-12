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
            Color(1, 0, 1, mode='hsv')
            d = 28.
            Ellipse(pos=(self.posX - d / 2, self.posY - d / 2), size=(d, d))

            x = self.posX
            y = self.posY

            if self.posX < self.goalX: self.posX = self.posX+1
            if self.posX > self.goalX: self.posX = self.posX-1
            if self.posY < self.goalY: self.posY = self.posY+1
            if self.posY > self.goalY: self.posY = self.posY-1
            
            Color(1, 0, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(self.posX - d / 2, self.posY - d / 2), size=(d, d))
            print('Pos X: %s Pos Y: %s' %(self.posX, self.posY))

class MyPaintApp(App):

    goingOn = False
    parent = MyPaintWidget()

    def build(self):        
        self.painter = MyPaintWidget()
        self.painter.setAgent()
        self.painter.setGoal()
        self.parent.add_widget(self.painter)
        startBtn = Button(text='START')
        stopBtn = Button(text='STOP', pos=(startBtn.width, 0))
        resetBtn = Button(text='RESET', pos=(startBtn.width*2, 0))
        startBtn.bind(on_release=self.start_experience)
        stopBtn.bind(on_release=self.stop_experience)
        resetBtn.bind(on_release=self.reset_experience)
        self.parent.add_widget(startBtn)
        self.parent.add_widget(stopBtn)
        self.parent.add_widget(resetBtn)
        return self.parent

    def start_experience(self, obj):
        if self.goingOn == False:
            Clock.schedule_interval(self.painter.update, 0.01)
            self.goingOn = True
        
    def stop_experience(self, obj):
        if self.goingOn == True:
            Clock.unschedule(self.painter.update)
            self.goingOn = False

    def reset_experience(self, obj):
        self.stop_experience(self)
        self.painter.canvas.clear()
        self.painter = MyPaintWidget()
        self.painter.setAgent()
        self.painter.setGoal()
        self.parent.add_widget(self.painter)

if __name__ == '__main__':
    MyPaintApp().run()