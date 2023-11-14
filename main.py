from turtle import Screen
from paddle import Pad
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

pad1 = Pad((370, 0))
pad2 = Pad((-370, 0))
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
    time.sleep(ball.update_speed)
    screen.update()

    ball.move()

    # ball bounce

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad1) < 50 and ball.xcor() > 350 or ball.distance(pad2) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    #     scores

    if ball.xcor() > 370:
        score.update_p2()
        ball.refresh()

    if ball.xcor() < -370:
        score.update_p1()
        ball.refresh()

screen.exitonclick()
