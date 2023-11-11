from turtle import Turtle


class Pad(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        for i in range(2):
            self.shape("square")
            self.color("white")
            self.shapesize(stretch_wid=3, stretch_len=0.5)
            self.penup()
            self.goto(coordinates)

    def up(self):
        new_ycor =self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)


