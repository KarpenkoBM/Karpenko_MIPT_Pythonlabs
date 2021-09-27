import turtle as t

t.shape('turtle')

def draw_2circles(r):
    k = 40
    for j in range(k):
        t.forward(r)
        t.left(360 / k)
        
    for i in range(k):
        t.forward(r)
        t.right(360 / k)
p = 1
while p <= 3 :
    draw_2circles(10)
    t.left(60)
    p = p + 1
        
        
