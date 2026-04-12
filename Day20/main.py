from turtle import Turtle, Screen
import time
import snake

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.tracer(0)

snake = snake.Snake()
sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")
game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()
sc.exitonclick()
