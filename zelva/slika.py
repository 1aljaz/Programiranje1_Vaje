import turtle
import colorsys

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

st_krogov = 36
st_velikih_krogov = 4
hue = 0

for i in range(st_krogov):
    t.color(colorsys.hsv_to_rgb(hue, 1, 1)) 
    for _ in range(st_velikih_krogov):
        t.circle(100)
        t.left(360 / st_velikih_krogov)
    t.right(360 / st_krogov)
    hue += 1 / st_krogov 


t.done()
