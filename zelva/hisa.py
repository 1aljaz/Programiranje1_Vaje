import turtle as t
import math
import random
import colorsys

s = t.Screen()
t = t.Turtle()
t.speed(10)

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
    hue = 0
    for i in range(n):
        t.penup()
        d = random.randint(20, 100)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        t.goto( t.pos() + (x, y))
        t.pendown()
        pobarvana_hisa(t, d, colorsys.hsv_to_rgb(hue, 1, 1) , colorsys.hsv_to_rgb(hue, 1, 1))
        t.setheading(0)
        hue += 1/n


# pobarvana_hisa(t, 100, 'red', 'blue')
vecHis(t, 8)
# hisa(t, 100)
s.exitonclick()
