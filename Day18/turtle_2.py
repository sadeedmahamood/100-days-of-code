from turtle import Turtle, Screen

tem = Turtle()
screen = Screen()

for _ in range(15):
  tem.pendown()
  tem.forward(10)
  tem.penup()
  tem.forward(10)
screen.exitonclick()