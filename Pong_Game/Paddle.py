from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.position = position
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.showturtle()
        self.ycor()
        self.xcor()

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.position[0], new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.position[0], new_y)
