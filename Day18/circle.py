from turtle import Turtle, Screen, colormode
import random

t = Turtle()
sc = Screen()
clr = colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color
t.speed(0)
def round(how_many):
  for _ in range(int(360 / how_many)):
    t.color(random_color())
    t.circle(100)
    # current_heading = t.heading()
    # t.setheading = current_heading + 10
    t.setheading(t.heading() + how_many)

round(3)
sc.exitonclick()
