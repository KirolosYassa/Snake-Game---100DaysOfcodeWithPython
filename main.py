from turtle import Screen
from SnakeBody import *
import time

LENGTH_SETUP = 600

screen = Screen()
screen.tracer(0)
screen.setup(width=LENGTH_SETUP, height=LENGTH_SETUP)
screen.title("Snake Game")
screen.bgcolor("black")
snakeBody = SnakeBody(5)
snake = snakeBody.snake

is_game_on = True

screen.onkey(snakeBody.up, "Up")
screen.onkey(snakeBody.right, "Right")
screen.onkey(snakeBody.left, "Left")
screen.onkey(snakeBody.down, "Down")
screen.listen()

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake[0].color("red")
    snake[0].pencolor("")
    snakeBody.move()


screen.exitonclick()
