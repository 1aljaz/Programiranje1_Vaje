import turtle as tu

def krivulja(t, n, fi, d):
    # Nariše Peanovo krivuljo
    if n == 0:
        return
    t.rt(fi)
    krivulja(t, n - 1, -fi, d)
    t.fd(d)
    krivulja(t, n - 1, fi, d)
    t.fd(d)
    krivulja(t, n - 1, -fi, d)
    t.lt(fi)


s = tu.Screen()

t = tu.Turtle()
tu.tracer(0)
t.speed(0)
t.lt(90)

krivulja(t, 6, 90, 10)

s.exitonclick()
