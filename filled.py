import math, turtle
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(50)

def findPoints(radius):
    for i in range(361):
        y = radius * math.sin(0.01745329 * i)
        x = radius * math.cos(0.01745329 * i)
        yield [x, y]

for i in findPoints(200):
    turtle.home()
    turtle.goto(i)