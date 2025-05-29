import turtle as tu
s = tu.Screen()
t = tu.Turtle()

def narisi(t, x, y, d, r, n):
    if n == 0:
        return 0

    s = 0
    dh = d / 2
    dv = d * r / 2

    xl, xd = x - dh, x + dh
    ys, yg = y - dv, y + dv

    # Vodoravna črta
    t.penup(); t.goto(xl, y)
    t.pendown(); t.goto(xd, y)
    s += d

    # Leva navpična črta
    t.penup(); t.goto(xl, ys)
    t.pendown(); t.goto(xl, yg)
    s += d * r

    # Desna navpična črta
    t.penup(); t.goto(xd, ys)
    t.pendown(); t.goto(xd, yg)
    s += d * r

    for nx, ny in [(xl, yg), (xl, ys), (xd, yg), (xd, ys)]:
        s += narisi(t, nx, ny, d / 2, r, n - 1)

    return s

def risi(n, o):
    r = o / 100
    d0 = 200

    t.speed(0)

    skupno = narisi(t, 0, 0, d0, r, n)
    print(f"vsota vseh crt: {skupno}")

tu.tracer(0)
risi(4, 80)

s.exitonclick()
