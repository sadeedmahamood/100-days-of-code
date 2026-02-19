from turtle import Turtle, Screen
import random

color = ['red','blue','green','orange','purple','yellow']

t = Turtle()
sc = Screen()

li = [0,90,180,270]

for _ in range(100):
  t.speed(0)
  t.pencolor(random.choice(color))
  t.pensize(5)
  t.forward(15)
  t.setheading(random.choice(li))
