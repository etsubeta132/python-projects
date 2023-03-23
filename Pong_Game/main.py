import time
from turtle import *

import Ball
from Ball import Ball
from Paddle import Paddle
from Score_Boared import Score_Boared

s = Screen()
s.setup(height=600, width=800)
s.bgcolor("black")
s.title("Pong Game")
s.tracer()
y = 280
while y >= -280:
    t = Turtle(shape="square")
    t.penup()
    t.hideturtle()
    t.color("white")
    t.shapesize(0.5)
    t.showturtle()
    t.goto(0, y)
    y -= 20

lp = Paddle((-350, 0))
rp = Paddle((350, 0))
ball = Ball()
s.listen()
s.onkey(fun=lp.move_up, key="q")
s.onkey(fun=lp.move_down, key="a")
s.onkey(fun=rp.move_up, key="Up")
s.onkey(fun=rp.move_down, key="Down")

sb = Score_Boared()
game_is_on = True
while game_is_on:
    time.sleep(ball.setspeed)
    s.update()
    ball.move()
    if ball.collide_with_wall():
        ball.bounce_y()

    # right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        sb.clear()
        sb.add_Lscore()

    # left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        sb.clear()
        sb.add_Rscore()

    # ball hits the  paddle
    if ball.distance(rp) < 50 and ball.xcor() > 320 or ball.distance(lp) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if sb.game_over():
        game_is_on = False
    else:
        game_is_on = True
















s.exitonclick()

