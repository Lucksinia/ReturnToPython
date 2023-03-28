import turtle
import time

turtle.setup(800, 600)
turtle.bgcolor("white")


def circles():
    turtle.speed(0)
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.setheading(0)

    colours = ["#FF0000", "#00FF00", "#0000FF"]

    for i in range(361):
        turtle.color(colours[i % 3])
        turtle.circle(100)
        turtle.left(1)


circles()

turtle.exitonclick()
