import turtle as t
import math

s = t.Screen()
t = t.Turtle()

def spirala(t, n):
    t.right(270)
    d = 10
    for i in range(n):
        t.forward(d)
        d+=10
        t.left(90)

spirala(t, 20)
s.exitonclick()