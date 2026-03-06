from turtle import Turtle, Screen
import random

tutle_on = False
sc = Screen()
sc.setup(width=500, height=400)
user_input =sc.textinput(title='Make your bet', prompt="Which tutle will win the race? select your color: ")
print(user_input)
color_t=['red','orange','blue','yellow','green','purple']
position = [ -80, -40, 0, 40, 80, 120]
all_turtle = []
for i in range(0,6):
    tom = Turtle(shape='turtle')
    tom.penup()
    tom.color(color_t[i])
    tom.goto(x=-230,y=position[i] )
    all_turtle.append(tom)

if user_input:
    turtle_on = True
while turtle_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            turtle_on = False
            winning_clr = turtle.pencolor()
            if winning_clr == user_input:
                print(f"you won! turele {winning_clr} win!!")
    
            else:
                print(f"you lose! turele {winning_clr} win!!")
        rand_num= random.randint(0,9)
        turtle.forward(rand_num)





     
sc.exitonclick()