from turtle import Turtle, Screen
import time
import snake
import food
import scoreboard

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.tracer(0)

snake = snake.Snake()
food = food. Food()
scoreaboard = scoreboard.Score()

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
    if snake.head.distance(food) < 15:
           food.rand_loc()
           snake.extend()
           scoreaboard.increse_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
          game_on = False
          scoreaboard.game_over()
    
    for seg in snake.all_tim[1:]:    
      if snake.head.distance(seg) < 10:
            game_on = False
            scoreaboard.game_over()

sc.exitonclick()
