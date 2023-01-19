from turtle import Turtle
LENGTH_SETUP = 600
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
EDGE = 0
COLORS = {
    "blue": 1,
    "red": 2,
    "yellow": 3,
}


class SnakeBody:

    def __init__(self, boxes=3):

        self.snake = []

        for i in range(boxes):
            # print(i)
            self.add_box((-DISTANCE*boxes, 0))

        self.head = self.snake[0]

    def add_box(self, position):
        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.pen(fillcolor="white", pencolor="")
        new_box.goto(position)
        new_box.speed("fastest")
        # print(new_box.pos())
        self.snake.append(new_box)

    def extend(self):
        self.add_box(self.snake[-1].position())

    def near_edge(self):
        if self.head.xcor() > (LENGTH_SETUP / 2) - EDGE or self.head.ycor() > (LENGTH_SETUP / 2) - EDGE:
            return True
        elif self.head.xcor() < (-LENGTH_SETUP / 2) - EDGE or self.head.ycor() < (-LENGTH_SETUP / 2) - EDGE:
            return True
        return False

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x_axis = self.snake[i - 1].xcor()
            y_axis = self.snake[i - 1].ycor()
            self.snake[i].goto(x=x_axis, y=y_axis)
        self.head.forward(distance=DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
