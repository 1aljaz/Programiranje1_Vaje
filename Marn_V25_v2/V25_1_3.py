import turtle

def narisi_plus(x, y, velikost):
    pol = velikost / 2
    turtle.penup()
    turtle.goto(x - pol, y)
    turtle.pendown()
    turtle.goto(x + pol, y)

    turtle.penup()
    turtle.goto(x, y - pol)
    turtle.pendown()
    turtle.goto(x, y + pol)
    turtle.penup()
    
    return velikost * 2

def rekurzija_plus(x, y, velikost, n):
    if n == 0 or velikost < 5:
        return 0

    zdejsnja = narisi_plus(x, y, velikost)
    
    nova_velikost = velikost / 2

    leva = rekurzija_plus(x - nova_velikost/2, y + nova_velikost/2, nova_velikost, n-1)
    desna = rekurzija_plus(x + nova_velikost/2, y - nova_velikost/2, nova_velikost, n-1)
    
    return zdejsnja + leva + desna

turtle.speed(0)
turtle.hideturtle()

total_length = rekurzija_plus(0, 0, 200, 4)
print(f"Skupna dolžina: {total_length}")

turtle.done()
