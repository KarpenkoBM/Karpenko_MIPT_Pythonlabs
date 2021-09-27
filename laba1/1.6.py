import turtle

turtle.shape('turtle')
n = 12
k = 1 
while k <= n :
    turtle.forward(50)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.left(360/n)
    k = k + 1
turtle.shape('circle')
