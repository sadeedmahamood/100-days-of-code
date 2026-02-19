import random
from turtle import Turtle, Screen

t = Turtle()
sc = Screen()
r = random.randint(000, 255)
g = random.randint(000, 255)
b = random.randint(000, 255)

dir = [0, 90, 180, 270]
for _ in range(100):
  t.pensize(5)
  t.pencolor(r , g , b)
  t.forward(15)
  t.setheading(random.choice(dir))



