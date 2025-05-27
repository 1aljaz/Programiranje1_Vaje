import turtle as t

s = t.Screen()
s.bgcolor("light gray")
t = t.Turtle()

t.pensize(5)  


t.left(90)
t.forward(100)
t.right(135)
t.forward(40)
t.left(90)
t.forward(40)
t.right(135)
t.forward(100)

t.penup()
t.left(90)
t.forward(40)
t.pendown()
t.left(90)
t.forward(100)
t.right(180)
t.forward(60)
t.left(90)
t.circle(30, 180)



s.exitonclick()