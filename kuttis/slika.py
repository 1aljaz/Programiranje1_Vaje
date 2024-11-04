from copy import deepcopy
from array import array 

def barvaj(x1, y1, x2, y2, b):
    base = y1 + x1
    y_range = range(max(0, y1), min(n, y2 + 1))
    x_range = range(max(0, x1), min(n, x2 + 1))
    
    for i in y_range:
        for j in x_range:
            if (i + j - base) & 1 == 0:
                canvas[j][i] = b

def load(num):
    canvas[:] = save[num]

n, k, m = map(int, input().split())
canvas = [[1] * n for _ in range(n)]
save = [deepcopy(canvas)]

commands = {
    "PAINT": lambda args: barvaj(*map(int, args)),
    "LOAD": lambda args: load(int(args[0])),
    "SAVE": lambda _: save.append(deepcopy(canvas))
}

for _ in range(m):
    cmd, *args = input().split()
    commands[cmd](args)

print('\n'.join(' '.join(map(str, row)) for row in canvas))