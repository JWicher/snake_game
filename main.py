from turtle import Screen
import time
from snake import Snake
from apple import Apple
from dashboard import Dashboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
apple = Apple()
dashboard = Dashboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(apple) < 15:
        apple.set_new_position()
        snake.increse_snake_size()
        dashboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        dashboard.game_over()
        game_is_on = False

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            dashboard.game_over()
            game_is_on = False


screen.exitonclick()
