import turtle as t
t.shape('turtle')
def star(n):
    a = 250
    for i in range(n):
        t.forward(a)
        t.right(180 - 180/n)
def moove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.speed(10)
moove(-300,0)
star(5)
moove(100,0)
star(11)
moove(500,500)
