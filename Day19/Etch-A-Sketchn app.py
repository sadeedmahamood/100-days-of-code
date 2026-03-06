from turtle import Turtle, Screen

tim = Turtle()
sc = Screen()


def move_forward():
    tim.forward(10)
def move_back():
    tim.backward(10)
def clock_wise():
    tim.left(10)
def anti_clock_wise():
    tim.right(10)
def circle():
    tim.circle(50)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


sc.listen()
sc.onkey(key='w',fun=move_forward)
sc.onkey(key='s',fun=move_back)
sc.onkey(key='d',fun=clock_wise)
sc.onkey(key='a',fun=anti_clock_wise)
sc.onkey(key='c',fun=circle)
# sc.onkey(key='v',fun=clear)
sc.onkey(clear,'v')
sc.exitonclick()