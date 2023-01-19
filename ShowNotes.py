from SnakeBody import *


class ShowNotes(Turtle):

    def __init__(self):
        super(ShowNotes, self).__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.home()
        self.setx((LENGTH_SETUP/2)-20)
        self.sety((-LENGTH_SETUP/2)+20)
        self.write(arg=f"Blue: 1\nRed: 2\nYellow: 3", align="right", font=('Courier', 8, 'normal'))
