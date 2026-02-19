from turtle import Turtle, Screen

tem = Turtle()
screen = Screen()

tem.pencolor('red')
for _ in range(3):
  tem.forward(100)
  tem.right(120)
tem.pencolor('red')
for _ in range(4):
  tem.forward(100)
  tem.right(90)
tem.pencolor('green')
for _ in range(5):
  tem.forward(100)
  tem.right(72)
tem.pencolor('brown')
for _ in range(6):
  tem.forward(100)
  tem.right(60)
tem.pencolor('blue')
for _ in range(7):
  tem.forward(100)
  tem.right( 51.5)
screen.exitonclick()
