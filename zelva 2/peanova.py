import turtle as tu

t = tu.Turtle()
s = tu.Screen()
t.speed(0)

def peanova_krivulja(t, dolz, n, orientacija=1):
    if n == 0:
        t.forward(dolz)
        return

    t.left(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, -orientacija)
    t.right(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, orientacija)
    t.right(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, orientacija)
    t.left(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, -orientacija)
    t.left(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, -orientacija)
    t.right(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, orientacija)
    t.right(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, orientacija)
    t.left(orientacija * 90)
    peanova_krivulja(t, dolz / 3, n - 1, -orientacija)



peanova_krivulja(t, 243, 3)
s.exitonclick()