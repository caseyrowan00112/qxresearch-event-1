from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


paddle = Turtle()
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off automatic animation; screen.update() redraws each frame

# Create the game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for keyboard input and control the paddles
screen.listen()
screen.onkey(r_paddle.go_Up, "Up")
screen.onkey(r_paddle.go_Down, "Down")
screen.onkey(l_paddle.go_Up, "w")
screen.onkey(l_paddle.go_Down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()

    # Bounce off either paddle
    hit_right_paddle = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    hit_left_paddle = ball.distance(l_paddle) < 50 and ball.xcor() < -320
    if hit_right_paddle or hit_left_paddle:
        ball.bounce_X()

    # Right paddle misses the ball: left player scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses the ball: right player scores
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
