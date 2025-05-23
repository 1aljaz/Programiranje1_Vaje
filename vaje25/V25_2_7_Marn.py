import turtle as tu

def sierpinski(t, d, n):
    # Nariše Sierpinskijevo preprogo stopnje n
    t.speed(0)
    if n == 0:
        return

    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.fd(d)
        t.lt(90)
    t.end_fill()
    t.penup()

    t.backward(2 * d / 3)
    t.rt(90)
    t.fd(2 * d / 3)
    t.lt(90)

    for _ in range(4):
        sierpinski(t, d / 3, n - 1)
        t.fd(d)
        sierpinski(t, d / 3, n - 1)
        t.fd(4 * d / 3)
        t.lt(90)

    t.fd(2 * d / 3)
    t.lt(90)
    t.fd(2 * d / 3)
    t.rt(90)

tu.tracer(0)
t = tu.Turtle()
t.penup()
sierpinski(t, 100, 5)
tu.done()
