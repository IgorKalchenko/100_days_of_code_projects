from turtle import Screen, Turtle
from time import sleep

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    sleep(ball.current_speed)
    screen.update()
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.current_speed = 0.1
        ball.bounce(wall=False)
        score.clear()
        score.increase_left()
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.current_speed = 0.1
        ball.bounce(wall=False)
        score.increase_right()
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce(wall=True)
    elif (ball.distance(right_paddle) < 60 and ball.xcor() > 320
          or ball.distance(left_paddle) < 60 and ball.xcor() < -320):
        ball.bounce(wall=False)