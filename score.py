from turtle import Turtle

coordinates = ((-50, 280), (50, 280))
line = (0, 300)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.count()
        self.sides()

    def sides(self):
        self.goto(line)
        self.color("white")
        for i in range(600):
            self.setheading(270)
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()

    def count(self):
        for i in range(len(coordinates)):
            self.goto(coordinates[i])
            self.write(f"score: {self.score}", align="center", font=("Arial", 16, "normal"))
