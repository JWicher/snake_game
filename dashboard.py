from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGN = 'center'

class Dashboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)