from turtle import Screen
from Food import *
from ScoreBoard import *
from ShowNotes import *
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=LENGTH_SETUP, height=LENGTH_SETUP)
screen.title("Snake Game")
screen.bgcolor("black")
snakeBody = SnakeBody()
snake = snakeBody.snake
food = Food()
score = ScoreBoard()
showNotes = ShowNotes()

is_game_on = True

screen.onkey(snakeBody.up, "Up")
screen.onkey(snakeBody.right, "Right")
screen.onkey(snakeBody.left, "Left")
screen.onkey(snakeBody.down, "Down")
screen.listen()
speed = 0.1

while is_game_on:
    screen.update()
    print(speed)
    time.sleep(speed)
    # snake[0].color("red")
    # snake[0].pencolor("")
    snakeBody.move()

    # Check updating score on eating food
    if snakeBody.head.distance(food) < 15:
        new_score = COLORS[food.color()[0]]
        for i in range(1, new_score+1):
            snakeBody.extend()
            score.add_in_score(score=1)
            if score.score % 5 == 0:
                speed -= 0.01

        food.refresh()

    # Check collision at walls
    if snakeBody.near_edge():
        print(f"Boom! Boom! at {snakeBody.head.pos()}")
        is_game_on = False

    # Check collision in snake body itself
    for snakeBox in snake[1:]:
        if snakeBody.head.distance(snakeBox) < 5:
            print(f"The snake touched itself at {snakeBox.pos()}")
            is_game_on = False

score.game_over()
screen.exitonclick()
