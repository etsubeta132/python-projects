import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setspeed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # self.setheading(60)
        self.goto(new_x, new_y)
        """self.setheading(-120)
        self.forward(800)
        self.setheading(120)
        self.forward(800)
        self.setheading(-60)
        self.forward(800)"""
    def collide_with_wall(self):
        if self.ycor() >= 290 or self.ycor() < -290:
            return True
        else:
            return False

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.setspeed *= 0.5

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.setspeed = 0.1
        self.showturtle()
        self.bounce_x()



