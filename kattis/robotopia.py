# https://open.kattis.com/problems/robotopia

def solve(l1, a1, l2, a2, lt, at):
    """
        Vrne število robotov enega tipa in drugega tipa, če je samo ena rešitev problema.
        Če je rešitev več, ali pa rešitve ni, vrne -1 -1.
    """
    mn = []
    
    max_i = min((lt - l2) // l1 if l1 > 0 else 10000, 
                 (at - a2) // a1 if a1 > 0 else 10000)
    
    for i in range(1, max_i + 1):
        if (lt - l1*i) % l2 == 0:
            j = (lt - l1*i) // l2
            
            if j > 0 and a1*i + a2*j == at:
                mn.append((i, j))

    if len(mn) == 1:
        return mn[0]
    return -1, -1


for _ in range(int(input())):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    
    x, y = solve(l1, a1, l2, a2, lt, at)
    if x > 0:
        print(x, y)
    else:
        print('?')