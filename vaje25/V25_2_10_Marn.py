import turtle as tu

def koch(t, dolzina, n):
    # Rekurzivno nariše n-to stopnjo Kochove snežinke
    if n > 0:
        for kot in [60, -120, 60, 0]:
            koch(t, dolzina / 3, n - 1)
            t.left(kot)
    else:
        t.forward(dolzina)

s = tu.Screen()
t = tu.Turtle()
t.speed(0)
tu.tracer(0)
d = 400
n = 7

for _ in range(3):
    koch(t, d, n)
    t.right(120)

s.exitonclick()
