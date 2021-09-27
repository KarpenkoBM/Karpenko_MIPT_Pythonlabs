import turtle as t
t.shape('turtle')

def draw_2halfcircles(r):
    k = 40
    for j in range(k):
        t.forward(r*5)
        t.right(180 / k)
    for j in range(k):
        t.forward(r)
        t.right(180 / k)
    
t.left(90)
t.penup()
t.goto(-250,0)
t.pendown()
p = 1
while p <= 4 :
    draw_2halfcircles(1)
    p = p + 1

for j in range(40):
        t.forward(5)
        t.right(180 / 40)
