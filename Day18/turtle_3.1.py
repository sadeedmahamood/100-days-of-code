from turtle import Turtle, Screen
import random

tim = Turtle()
sc = Screen()

# shape = 3
# for _ in range(shape):
#   angle = (360 / shape)
#   tim.forward(100)
#   tim.right(angle)

color = ['red','green', 'blue', 'purple']

def draw(numm):
  angle = (360 / numm)
  for _ in range(numm):
    tim.forward(100)
    tim.right(angle)

for i in range(3,8):
  tim.pensize(4)
  tim.color(random.choice(color))
  draw(i)
