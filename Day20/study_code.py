from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")

# position = [0,20,40]

# for i in range(0,3):
#     tom = Turtle()
#     tom.shape('square')
#     tom.color("white")
#     tom.goto(x=position[i], y=0)


position = [(0,0), (20, 0), (40,0)]
for pos in position:
    tim = Turtle("square")
    tim.color("white")
    tim.goto(pos)




sc.exitonclick()