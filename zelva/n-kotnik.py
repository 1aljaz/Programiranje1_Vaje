import turtle as t
import math

s = t.Screen()
t = t.Turtle()

def nKotnik(t, n, d, barva):
    fi = 360/n
    if barva:
        t.fillcolor(barva)
        t.begin_fill()
    for i in range(n):
        t.right(fi)
        t.forward(d)
    t.end_fill()
    

nKotnik(t, 10, 100, None)
s.exitonclick()