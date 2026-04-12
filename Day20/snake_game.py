from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")

def rand_loc():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    co_odi = (x, y)
    print(co_odi)

tim = Turtle()
tim.shape("square")
tim.color("white")


fod = Turtle()
fod.shape("circle")
fod.color("blue")
fod.penup()
# fod.goto(x=250, y=170)
fod.goto(rand_loc)

sc.exitonclick()