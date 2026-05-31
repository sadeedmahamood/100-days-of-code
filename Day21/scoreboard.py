from turtle import Turtle
FONT = ('arial', 15, 'normal')
ALIGN = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!', align=ALIGN, font=FONT)

    def increse_score(self):
        self.score += 1 
        self.clear()
        self.update_score()
