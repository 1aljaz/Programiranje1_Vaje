def preveri(arr:list, k:int)->bool:
    for i in range(2, k):
        skupaj = arr[i-2] + arr[i-1]
        if skupaj < arr[i]:
            return False
    return len(arr) >= k

n, k = map(int, input().split())

tezavnost = []

for i in range(n):
    tezavnost.append(int(input()))

tezavnost.sort()

