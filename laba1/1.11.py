import turtle as t

t.shape('turtle')
t.speed(20)

def draw_2circles(r):
    k = 40
    for j in range(k):
        t.forward(r)
        t.left(360 / k)
        
    for i in range(k):
        t.forward(r)
        t.right(360 / k)
p = 1
t.left(90)
while p <= 10 :
        draw_2circles(8 + 2 * p)
        p = p + 1
