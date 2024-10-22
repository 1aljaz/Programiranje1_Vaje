# https://open.kattis.com/problems/slika
save = [[]]

def printc():
    for i in range(n):
        for j in range(n):
            try:
                print(canvas[i][j], end=" ")
            except:
                print()
        print()
    print()

def barvaj(x1, y1, x2, y2, b):
   for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    if 0 <= i < n and 0 <= j < n:
                        if (i - y1 + j - x1) % 2 == 0:
                            canvas[j][i] = b

def load(num):
   print(save[num])

t = input()
n, k, m = t.split()

n = int(n)
k = int(k)
m = int(m)

canvas = [[1 for _ in range(n)] for _ in range(n)]

for i in range(m):
    printc()
    t = input()
    try: # PAINT
        command, b, x1, y1, x2, y2 = t.split()

        barvaj(int(x1), int(y1), int(x2), int(y2), int(b))
        continue
    except:
        try: # LOAD
            command, num = t.split()
            num = int(num)
            print(save[num])
            printc()
            continue
        except: # SAVE
            command = t
            save.append(canvas)
            continue

printc()



