# https://open.kattis.com/problems/robotopia

def solve(l1, a1, l2, a2, lt, at):
    """
        Vrne število robotov enega tipa in drugega tipa, če je samo ena rešitev problema.
        Če je rešitev več, ali pa rešitve ni, vrne -1 -1.
    """
    mn = []
    
    # izračunamo zgornjo mejo robotov prvega tipa
    M_i = min((lt - l2) // l1, (at - a2) // a1)
    
    for i in range(1, M_i + 1): # i predstavlja robote prvega tipa
        if (lt - l1*i) % l2 == 0:
            # j predstavlja robote drugega tipa
            j = (lt - l1*i) // l2
            
            if j > 0 and a1*i + a2*j == at:
                mn.append((i, j)) 

    if len(mn) == 1:
        return mn[0] # Rešitev obstaja
    return -1, -1 # Rešitev ne obstaja. Ali jih je preveč ali je pa ni.


for _ in range(int(input())):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    
    x, y = solve(l1, a1, l2, a2, lt, at)
    if x > 0:
        print(x, y)
    else:
        print('?')