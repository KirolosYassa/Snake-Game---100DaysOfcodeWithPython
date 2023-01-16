from turtle import Screen
from SnakeBody import *
lenght_setup = 600

screen = Screen()
screen.setup(width=lenght_setup,height=lenght_setup)
screen.title("Snake Game")
screen.bgcolor("black")
snake = SnakeBody()


screen.exitonclick()

