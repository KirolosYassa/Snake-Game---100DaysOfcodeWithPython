from SnakeBody import *
import random as r


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = r.randint(a=-LENGTH_SETUP/2 + 20, b=LENGTH_SETUP/2 - 20)
        random_y = r.randint(a=-LENGTH_SETUP/2 + 20, b=LENGTH_SETUP/2 - 20)
        colors = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "red", "red", "yellow"]
        random_color = r.choice(colors)
        self.color(random_color)
        self.goto(x=random_x, y=random_y)
