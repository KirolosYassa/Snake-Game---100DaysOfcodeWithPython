from turtle import Turtle


class SnakeBox:

    def __init__(self):
        self.self = Turtle(shape="square")
        self.self.color("white")
        self.self.pen(fillcolor="white", pencolor="")
        # self.self.shapesize(.8)

    def pos(self):
        return self.self.pos()

    # def goto(self, x, y=None):
    #     self.self.goto(x=x, y=y)

    def setx(self, xcor):
        self.self.setx(x=xcor)
