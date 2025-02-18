# https://open.kattis.com/problems/fleaonachessboard

def je_na_belem(x:int, y:int, S:int):
    """Vrne True, če je bolha priletela na bel kvadrat in False če ni."""
    desno = x // S
    gor = y // S
    if (desno + gor) % 2 == 1: # Kvadrat je bel, ce ko se vrstica in stolpec sestejeta je stevilka liha.
        return True
    return False

while True:

    S, x, y, dx, dy = map(int, input().split())
    n = 0

    if S==x==y==dx==dy==0:
        break
    while True:
        if je_na_belem(x,y, S):
            print (f"After {n} jumps the flea lands at ({x}, {y}).")
            break
        if (dx+dy) % 2 == 0 and (x+y) % 2 == 1:
            print ("The flea cannot escape from black squares.")
            break
        n+=1
        x+=dx
        y+=dy