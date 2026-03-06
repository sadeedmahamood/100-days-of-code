from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
Sc = Screen()

tim.color("red")
tim.setheading(180)
tim.penup()
tim.forward(100)
tim.pendown()
tim.setheading(0)
tom.color("blue")
tom.setheading(0)
tom.penup()
tom.forward(100)
tom.pendown()
tom.setheading(180)
Sc.exitonclick()