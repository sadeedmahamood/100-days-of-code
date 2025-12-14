from turtle import Turtle,Screen

Timmy = Turtle() #new Object
print(Timmy) 
Timmy.shape("turtle") #method
Timmy.color("red")  #method
Timmy.forward(100)  #method

screen_size = Screen()
print(screen_size.canvheight) #attribute by using object
screen_size.exitonclick() #method
