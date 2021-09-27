import turtle

turtle.shape('turtle')
n = 1
x = 0
y = 0
turtle.goto(x,y)
while n <= 10 :
    turtle.forward(50 * n)
    turtle.left(90)
    turtle.forward(50 * n)
    turtle.left(90)
    turtle.forward(50 * n)
    turtle.left(90)
    turtle.forward(50 * n)
    turtle.penup()
    x = x - 25
    y = y - 25
    turtle.goto(x, y)
    turtle.left(90)
    turtle.pendown()
    n = n + 1
exitonclick() 
    
