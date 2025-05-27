import turtle as tu

t = tu.Turtle()
s = tu.Screen()

def stranica(t, n, dolz):
    if n == 1:
        t.fd(dolz)
        return dolz
    else:
        t.fd(dolz / 3)
        t.left(90)
        t.fd(dolz / 3)
        t.right(90)
        obseg = stranica(t, n-1, dolz / 3)
        t.right(90)
        t.fd(dolz / 3)
        t.left(90)
        t.fd(dolz / 3)
        return obseg + 4/3 * dolz

def kvadrat(t, n, dolz):
    obseg = 0
    for i in range(4):
        obseg += stranica(t, n, dolz)
        t.right(90)
    return obseg

o = kvadrat(t, 4, 300)
print(o)
s.exitonclick()

