# Problem: https://open.kattis.com/problems/bank

n, t = map(int, input().split())

ljudje = [[0, 0] for _ in range(n)]
obiskane = [0] * n

for i in range(n):
    ljudje[i][0], ljudje[i][1] = map(int, input().split())

rezultat = 0

# Gremo od minute t navzdol do minute 0
while t >= 0:
    mx = -1
    for i in range(n):
        # Najdem človeka za tisto minuto, ki ima največ denarja in je še ostal
        if not obiskane[i] and ljudje[i][1] >= t and (mx == -1 or ljudje[i][0] > ljudje[mx][0]):
            mx = i # v mx je izbrana oseba
    
    # Če sem osebo našel jo označim za obiskano in njen denar dodam v banko
    if mx != -1:
        rezultat += ljudje[mx][0]
        obiskane[mx] = 1
    
    t -= 1

print(rezultat)
