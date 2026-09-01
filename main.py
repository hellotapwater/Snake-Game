from turtle import Screen
import turtle as t
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

# My version of Snake Game
screen = Screen()
tim = t.Turtle()
tim.home()
tim.color("white")
tim.shape("square")
screen.clear()



screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)
screen.bgcolor("black")


all_turtles = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    

    for segments in snake.all_turtles[2:-1]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()








