from turtle import Turtle

coordinates = ((-50, 250), (50, 250))
line = (0, 300)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.p1_score = 0
        self.p2_score = 0
        self.count()

    def count(self):
        self.clear()
        self.goto(coordinates[0])
        self.write(f"{self.p1_score }", align="center", font=("Arial", 26, "normal"))
        self.goto(coordinates[1])
        self.write(f"{self.p2_score}", align="center", font=("Arial", 26, "normal"))

    def update_p1(self):
        self.p1_score += 1
        self.count()

    def update_p2(self):
        self.p2_score += 1
        self.count()
