from turtle import Turtle


class Score_Boared(Turtle):
    def __init__(self):
        super().__init__()
        self.RScore = 0
        self.LScore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(f"{self.LScore}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.RScore}", align="center", font=("Courier", 80, "normal"))

    def add_Rscore(self):
        self.RScore += 1
        self.update_score()

    def add_Lscore(self):
        self.LScore += 1
        self.update_score()

    def game_over(self):
        if self.LScore == 5 and self.RScore == 0 or self.LScore == 10 and self.RScore < 10:
            self.goto(0, 0)
            self.write(f"Game over \n The left player wins by {self.LScore}:{self.RScore}",
                       align="center", font=("Courier", 24, "normal"))
            return True
        elif self.RScore == 5 and self.LScore == 0 or self.RScore == 10 and self.LScore < 10:
            self.goto(0, 0)
            self.write(f"Game over \n The Right player wins by {self.RScore}:{self.LScore}",
                       align="center", font=("Courier", 24, "normal"))
            return True
        else:
            return False




