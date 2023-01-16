from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class SnakeBody:

    def __init__(self, boxes=3):

        self.snake = []

        for i in range(boxes):
            new_box = Turtle(shape="square")
            new_box.color("white")
            new_box.pen(fillcolor="white", pencolor="")
            new_box.setheading(0)
            new_box.speed("fastest")
            self.snake.append(new_box)

        self.head = self.snake[0]
        start_index = DISTANCE
        for box in self.snake:
            print(f"before: {box.pos()}")
            # cor = (start_index-distance)
            box.setx(start_index - DISTANCE)
            print(f"after: {box.pos()}")
            start_index -= DISTANCE

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
