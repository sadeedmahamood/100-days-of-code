from turtle import Turtle
POSITION = [(0,0), (-20, 0), (-40,0)]
MOVE_POSITION = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_tim = []
        self.create_snake()
        self.head = self.all_tim[0]
    def create_snake(self):
        for pos in POSITION:
            self.add_segment(pos)
    def add_segment(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.all_tim.append(tim) 

    def extend(self):
        self.add_segment(self.all_tim[-1].pos())

    def move(self):        
        for tt in range(len(self.all_tim) - 1,0, -1):
            x = self.all_tim[tt - 1].xcor()
            y = self.all_tim[tt - 1].ycor()
            self.all_tim[tt].goto(x,y)
        self.head.forward(MOVE_POSITION)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.setheading(RIGHT):
            self.head.setheading(RIGHT)
