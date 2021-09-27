import turtle as t
from random import *
t.shape('circle')
t.speed(10)
def moove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def draw_num(num):
    x = t.xcor()
    y = t.ycor()
    for i in range(0, len(num), 2) :
        x += num[i]
        y += num[i+1]
        if (i == 0) or (i == len(num)- 2) :
            moove(x,y)
        else :
            t.goto(x,y)
        
def ex_1():
 t.color('red')
 for i in range(100) :
        t.forward(random() * 100)
        t.left(random() * 360)
def ex_2():
    moove(-375, 0)
    n_0 = [0, 0, 40, 0, 0, -80, -40, 0, 0, 80, 80, 0]
    n_1 = [0, -40, 40, 40, 0, -80, 40, 80]
    n_2 = [0, 0, 40, 0, 0, -40, -40, -40, 40, 0, 40, 80]
    n_3 = [0, 0, 40, 0, -40, -40, 40, 0, -40, -40, 80, 80]
    n_4 = [0, 0, 0, -40, 40, 0, 0, -40, 0, 80, 40, 0]
    n_5 = [40, 0, -40, 0, 0, -40, 40, 0, 0, -40, -40, 0, 80, 80]
    n_6 = [40, 0, -40, -40, 0, -40, 40, 0, 0, 40, -40, 0, 80, 40]
    n_7 = [0, 0, 40, 0, -40, -40, 0, -40, 80, 80]
    n_8 = [0, 0, 40, 0, 0, -40,-40, 0, 0, -40, 40, 0, 0, 40, -40, 0, 0, 40, 80, 0]
    n_9 = [0, -80, 40, 40, 0, 40, -40, 0, 0, -40, 40, 0, 40, 40]
    num = [n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9]
    el = list(map(int, input(('Какой набор чисел вы хотите увидеть?')).split()))
    print(el)
    for j in range(len(el)) :
        draw_num(num[el[j]])
    moove(1000, 10000)
def ex_3():
    moove(-375, 0)
    inp = open('Numbers_turtle.txt', 'r')
    num = []
    for i in range(10):
        num.append([int(n) for n in inp.readline().rstrip().split(', ')])
    inp.close()
    el = list(map(int, input(('Какой набор чисел вы хотите увидеть?')).split()))
    print(el)
    for j in range(len(el)) :
        draw_num(num[el[j]])
    moove(1000, 10000)
def ex_4():
    x = -375
    y = 0
    t.goto(-x,y)
    t.goto(x,y)
    Vmax = 40
    Vy = 40
    Vx = 20
    dt = 0.1
    i = 1
    while Vmax > 0 :
        x += Vx*dt 
        y += Vy*dt + - 10*dt**2 / 2
        Vy += -10*dt
        Vx += -0.05
        if y < 0 :
            i +=1
            Vmax = Vmax - 5
            Vy = Vmax
            y = 0
        t.goto(x,y)
def ex_5():
    t.hideturtle()
    moove(-210,250)
    t.goto(-210,-250)
    t.goto(210,-250)
    t.goto(210,250)
    t.goto(-210,250)
    t.shape
    number_of_turtles = 40
    steps_of_time_number = 100
    a = 5
    x=[]
    y=[]
    vx=[]
    vy=[]
    gas = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
    for unit in gas:
        unit.turtlesize(0.5)
        unit.color(random(),random(),random())
        unit.penup()
        unit.speed(0)
        x.append(randint(-200, 200))
        y.append(randint(-200, 200))
        vx.append(randint(-10,10))
        vy.append(randint(-10,10))
        unit.goto(x[-1], y[-1]) 
    for i in range(steps_of_time_number):
        for unit in gas:
            r = gas.index(unit)
            x[r] += vx[r]
            y[r] += vy[r]
            if abs(x[r])>=200:
                vx[r] = -vx[r]
            if abs(y[r])>=240:
                vy[r] = -vy[r]
            unit.goto(x[r],y[r])

     
r = int(input('Какую задачу вы хотите увидеть?'))
if r == 1 :
    ex_1()
elif r == 2:
    ex_2()
elif r == 3:
    ex_3()
elif r == 4:
    ex_4()
elif r == 5:
    ex_5()



 
        
        

            
        


