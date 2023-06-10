from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()


# Key binding
s.listen()
s.onkey(key="w", fun=snake.up)
s.onkey(key="s", fun=snake.down)
s.onkey(key="a", fun=snake.left)
s.onkey(key="d", fun=snake.right)


start_game = True

while start_game:
    s.update()
    time.sleep(0.12)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        score.updateScore()
        food.newFood()
        snake.grow_snake()

    # detect collision with WALL
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        start_game = False
        score.game_over()

    # detect collision with tail
    for seg in snake.snake[1:]:
        if snake.snake_head.distance(seg) < 10:
            start_game = False
            score.game_over()


s.exitonclick()
