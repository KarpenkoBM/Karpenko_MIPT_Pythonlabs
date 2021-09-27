import turtle as t
from math import tan, sqrt, pi
i = 0
x = 3
while x <= 13:
        t.circle(10 + i, 360, x)
        t.penup()
        t.goto(0, -10-i)
        x = x + 1
        t.pendown()
        i = i + 10
                
