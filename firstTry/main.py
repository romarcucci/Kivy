from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label

class MyPaintWidget(Widget):
    posX = 0
    posY = 0
    goalX = 0
    goalY = 0

    dir = 0
    const = 0

    trace = 0

    def setAgent(self):
        with self.canvas:
            self.posX = round(random() * 670 + 40)
            self.posY = round(random() * 410 + 110 + 40)
            self.goalX = round(random() * 670 + 40)
            self.goalY = round(random() * 410 + 110 + 40)
            Color(1, 0, 1, mode='hsv')
            Rectangle(pos=(5, 110), size=(740, 1))
            Rectangle(pos=(5, 110), size=(1, 490))
            Rectangle(pos=(5, 599), size=(740, 1))
            Rectangle(pos=(744, 110), size=(1, 490))

            Rectangle(pos=(410, 10), size=(335, 1))
            Rectangle(pos=(410, 99), size=(335, 1))
            Rectangle(pos=(410, 10), size=(1, 90))
            Rectangle(pos=(744, 10), size=(1, 90))

            Label(
                text='Pos  X: %3d             Pos  Y: %3d \n\nGoal X: %3d             Goal Y: %3d'
                %(self.posX, self.posY, self.goalX, self.goalY), 
                pos=(480, 10))

            d = 30.
            Ellipse(pos=(self.posX, self.posY), size=(d, d))
            self.trace = Line(points=(self.posX + d/2, self.posY + d/2))
            print('Pos X: %s Pos Y: %s' %(self.posX, self.posY))
            self.dir = (self.goalY - self.posY)/(self.goalX - self.posX)
            self.const  = self.posY - self.dir*self.posX
            print('dir: %s const: %s' %(self.dir, self.const))

    def setGoal(self):
        with self.canvas:
            Color(0, 1, 1, mode='hsv')
            d = 30.
            Ellipse(pos=(self.goalX, self.goalY), size=(d, d))
            print('Goal X: %s Goal Y: %s' %(self.goalX, self.goalY))
    
    def update(self, dt):
        with self.canvas:
            self.canvas.clear()
            self.setGoal()

            if self.posX != self.goalX or self.posY != self.goalY:
                if self.posX < self.goalX: self.posX += 1
                if self.posX > self.goalX: self.posX -= 1
                self.posY = round(self.dir*self.posX + self.const)

            Color(1, 0, 1, mode='hsv')
            Rectangle(pos=(5, 110), size=(740, 1))
            Rectangle(pos=(5, 110), size=(1, 490))
            Rectangle(pos=(5, 599), size=(740, 1))
            Rectangle(pos=(744, 110), size=(1, 490))

            Rectangle(pos=(410, 10), size=(335, 1))
            Rectangle(pos=(410, 99), size=(335, 1))
            Rectangle(pos=(410, 10), size=(1, 90))
            Rectangle(pos=(744, 10), size=(1, 90))

            Label(
                text='Pos  X: %3d             Pos  Y: %3d \n\nGoal X: %3d             Goal Y: %3d'
                %(self.posX, self.posY, self.goalX, self.goalY), 
                pos=(480, 10))
            
            d = 30.
            Ellipse(pos=(self.posX, self.posY), size=(d, d))
            self.trace.points += [self.posX + d/2, self.posY + d/2]
            Line(points = self.trace.points)
            print('Pos X: %s Pos Y: %s' %(self.posX, self.posY))

class MyPaintApp(App):

    goingOn = False
    parent = MyPaintWidget()

    def build(self):
        
        Window.size = (750, 610)
        Config.set('graphics', 'resizable', False)
        self.painter = MyPaintWidget()
        self.painter.setAgent()
        self.painter.setGoal()
        self.parent.add_widget(self.painter)
        
        startBtn = Button(text='START', pos=(5,5))
        stopBtn = Button(text='STOP', pos=(startBtn.width + 5, 5))
        resetBtn = Button(text='RESET', pos=(startBtn.width*2 + 5, 5))
        quitBtn = Button(text='QUIT', pos=(startBtn.width*3 + 5, 5))

        startBtn.bind(on_release=self.start_experience)
        stopBtn.bind(on_release=self.stop_experience)
        resetBtn.bind(on_release=self.reset_experience)
        quitBtn.bind(on_release=self.quit_app)
        
        self.parent.add_widget(startBtn)
        self.parent.add_widget(stopBtn)
        self.parent.add_widget(resetBtn)
        self.parent.add_widget(quitBtn)
        
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
    
    def quit_app(self, obj):
        self.get_running_app().stop()

if __name__ == '__main__':
    MyPaintApp().run()