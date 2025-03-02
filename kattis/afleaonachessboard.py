# https://open.kattis.com/problems/fleaonachessboard

def je_na_belem(x:int, y:int, S:int):
    """Vrne True, če je bolha priletela na bel kvadrat in False če ni."""
    # Handle edge case when flea is on border
    if x % S == 0 or y % S == 0:
        return False
        
    desno = x // S
    gor = y // S
    if (desno + gor) % 2 == 1:  # Kvadrat je bel, ce ko se vrstica in stolpec sestejeta je stevilka liha.
        return True
    return False

while True:
    S, x, y, dx, dy = map(int, input().split())
    
    if S == x == y == dx == dy == 0:
        break
        
    # Check initial position first
    if je_na_belem(x, y, S):
        print(f"After 0 jumps the flea lands at ({x}, {y}).")
        continue
        
    n = 1
    start_x, start_y = x, y
    while True:
        # Make the jump
        x += dx
        y += dy
        
        if je_na_belem(x, y, S):
            print(f"After {n} jumps the flea lands at ({x}, {y}).")
            break
            
        # Check if we've returned to a previously visited position
        if n > 100000 or (n > 4 and x % S == start_x % S and y % S == start_y % S):
            print("The flea cannot escape from black squares.")
            break
            
        n += 1