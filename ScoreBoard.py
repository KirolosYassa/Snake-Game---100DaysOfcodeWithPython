from SnakeBody import *
import time

FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.home()
        self.sety(LENGTH_SETUP/2 - 30)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", align="center", font=FONT)

    def add_in_score(self, score=1):
        self.score += score
        self.update_score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score_board()
