import turtle as t
import math

t.speed(10)

def heksa(t, d):
    fi = 360/6
    for i in range(6):
        t.forward(d)
        t.right(fi)

def heksagons(t, d):
    poz = []
    fi = 360/6
    for i in range(6):
        t.forward(d)
        t.right(fi)
        poz.append(t.pos())

    for i in range(6):
        t.goto(poz[i])
        t.setheading(fi + i*180)
        heksa(t, d)
    
    t.goto(0, 0)
    t.setheading(0)
    for i in range(6):
        t.forward(d)
        t.left(fi)
    t.penup()
    t.goto(0, -d*math.sqrt(3))
    t.pendown()
    heksa(t, d)




heksa(t, 30)
t.exitonclick()
