import random
import time
import turtle

turtle.tracer(1000, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

def narisiPoganjek(zacetek, smer, dolzina):
    if dolzina < 5:
        return

    turtle.penup()
    turtle.goto(zacetek)
    turtle.setheading(smer)

    turtle.pendown()
    turtle.pensize(max(dolzina / 7, 1))
    turtle.forward(dolzina)

    konec = turtle.position()
    leva_smer = smer + levi
    leva_dolzina = dolzina - leva_manjsanje
    desna_smer = smer - desni
    desna_dolzina = dolzina - desna_manjsanje

    narisiPoganjek(konec, leva_smer, leva_dolzina)
    narisiPoganjek(konec, desna_smer, desna_dolzina)


levi = random.randint(10, 30)
leva_manjsanje  = random.randint(8, 15)
desni = random.randint(10, 30)
desna_manjsanje = random.randint(8, 15)
zacetna_dolzina = random.randint(80, 120)


turtle.clear()
turtle.penup()
turtle.goto(10, 10)


narisiPoganjek((350, 10), 90, zacetna_dolzina)

turtle.done()
