from SnakeBody import *
import time

FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.home()
        self.sety(LENGTH_SETUP/2 - 30)
        self.update_score_board()

    def update_score_board(self):
        self.write(arg=f"Score = {self.score}", align="center", font=FONT)

    def add_in_score(self, score=1):
        self.score += score
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.sety(0)
        self.write(arg=f"Game Over.", align="center", font=FONT)

