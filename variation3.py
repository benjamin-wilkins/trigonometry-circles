import math, turtle
turtle = turtle.Turtle()
turtle.speed(0)

def findPoints(radius):
    for i in range(361):
        y = radius * math.sin(0.01745329 * i)
        x = radius * math.cos(0.01745329 * i)
        yield [x, y]

points = list(findPoints(200))
for i in range(180):
        turtle.goto(points[i])
        turtle.goto(points[-i])