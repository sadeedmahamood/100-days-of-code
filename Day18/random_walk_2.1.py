import random
from turtle import Turtle, Screen, colormode

t = Turtle()
col = colormode(255)
sc = Screen()
def color_mode():
  r = random.randint(000, 255)
  g = random.randint(000, 255)
  b = random.randint(000, 255)
  random_color = (r, g, b)
  return random_color


dir = [0, 90, 180, 270]
for _ in range(100):
  t.pensize(5)
  t.color(color_mode())
  t.speed(0)
  t.forward(15)
  t.setheading(random.choice(dir))



