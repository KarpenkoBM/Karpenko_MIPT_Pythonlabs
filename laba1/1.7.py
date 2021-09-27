from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(500):
    t = i / 50 * pi
    x = t * cos(t)
    y = t * sin(t)
    turtle.goto(x, y)
