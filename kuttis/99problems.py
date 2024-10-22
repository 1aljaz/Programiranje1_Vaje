p:int

def ending(a:int):
    if a < 0:
        return False
    if a % 100 == 99:
        return True
    return False

p = int(input())
u = d = p

while True:
    if ending(u):
        print(u)
        break
    
    if ending(d):
        print(d)
        break
    u+=1
    d-=1
