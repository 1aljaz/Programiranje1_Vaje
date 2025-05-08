import turtle as t
import math
import random

s = t.Screen()
t = t.Turtle()

def hisa(turtle, velikost):
    
    turtle.forward(velikost)
    turtle.right(90)
    turtle.forward(velikost)
    turtle.right(90)
    turtle.forward(velikost)
    turtle.right(90)
    turtle.forward(velikost)
    turtle.right(45)
    kateta = velikost / math.sqrt(2)
    turtle.forward(kateta)
    turtle.right(90)
    turtle.forward(kateta)

def pobarvana_hisa(t, velikost, fasada, streha):
    t.fillcolor(fasada)
    t.begin_fill()
    t.forward(velikost)
    t.right(90)
    t.forward(velikost)
    t.right(90)
    t.forward(velikost)
    t.right(90)
    t.forward(velikost)
    t.right(45)
    t.end_fill()
    t.fillcolor(streha)
    kateta = velikost / math.sqrt(2)
    t.begin_fill()
    t.forward(kateta)
    t.right(90)
    t.forward(kateta)
    t.end_fill()

def vecHis(t, n):
    for i in range(n):
        t.penup()
        d = random.randint(20, 50)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        t.goto( t.pos() + (x, y))
        t.pendown()
        pobarvana_hisa(t, )


vecHis(t, 10)
s.exitonclick()
