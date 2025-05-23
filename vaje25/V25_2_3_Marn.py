import turtle as tu

def zmaj(t, n, kot, d):
    # Itriše tmajnico
    if n < 1:
        t.fd(d)
        return
    zmaj(t, n - 1, 90, d)
    t.rt(kot)
    zmaj(t, n - 1, -90, d)

t = tu.Turtle()
s = tu.Screen()
t.speed(0)
tu.tracer(0)
zmaj(t, 15, 90, 2)

s.exitonclick()

