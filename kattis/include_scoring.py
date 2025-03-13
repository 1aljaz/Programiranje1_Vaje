class Contestant:
    def __init__(self, score, i, extra):
        self.score = score
        self.i = i
        self.extra = extra
    
    def __str__(self):
        return f"{self.score}, {self.i}"

    def __lt__(self, other):
        return self.score > other.score

n = int(input())
con = []
mesta = {
    1: 100, 2: 75, 3: 60, 4: 50, 5: 45,
    6: 40, 7: 36, 8: 32, 9: 29, 10: 26,
    11: 24, 12: 22, 13: 20, 14: 18, 15: 16,
    16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
    21: 10, 22: 9, 23: 8, 24: 7, 25: 6,
    26: 5, 27: 4, 28: 3, 29: 2, 30: 1
}

for i in range(n):
    s, p, f, o = map(int, input().split())
    con.append(Contestant(s*10**12 - p*10**6 - f, i, o))

con.sort()
result = [0] * n

i = 0
while i < n:
    j = i + 1
    while j < n and con[j].score == con[i].score:
        j += 1
    
    if j - i > 1:
        total_score = 0
        for rank in range(i + 1, min(j + 1, 31)):
            total_score += mesta.get(rank, 0)
            
        avg_score = (total_score + mesta.get(i + 1, 0)) // (j - i)
        if (total_score + mesta.get(i + 1, 0)) % (j - i) != 0:
            avg_score += 1
            
        for k in range(i, j):
            result[con[k].i] = avg_score + con[k].extra
    else:
        rank = i + 1
        if rank <= 30:
            result[con[i].i] = mesta[rank] + con[i].extra
        else:
            result[con[i].i] = con[i].extra
    
    i = j

for score in result:
    print(score)