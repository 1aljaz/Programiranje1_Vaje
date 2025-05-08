import turtle as t
import math

s = t.Screen()
t = t.Turtle()

def zelva(t, pot, d):
    angle = (0, 0) # trenuten, hoten
    for c in pot:
        if c == 'u':
            t.setheading(90)
        if c == 'r':
            t.setheading(0)
        if c == 'l':
            t.setheading(180)
        if c == 'd':
            t.setheading(270)
        
        t.forward(d)

zelva(t, 'ururullldldr', 40)
s.exitonclick()
        