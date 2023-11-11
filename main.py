from turtle import Screen
from paddle import Pad
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

pad1 = Pad((280, 0))
pad2 = Pad((-280, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
screen.onkey(pad2.up, "w")
screen.onkey(pad2.down, "s")

Game_on = True
while Game_on:
    # updates the screen and slows down the time
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
