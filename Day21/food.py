from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.rand_loc()

    def rand_loc(self):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        # loca = (x, y)
        # return loca
        self.goto(x, y)
