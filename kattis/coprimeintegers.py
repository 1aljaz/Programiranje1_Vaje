from math import gcd

def prestej(a, b, c, d):
    if (b - a + 1) * (d - c + 1) <= 10000:
        count = 0
        for i in range(a, b + 1):
            for j in range(c, d + 1):
                if gcd(i, j) == 1:
                    count += 1
        return count
    
    total_pairs = (b - a + 1) * (d - c + 1)
    max_val = max(b, d)

    mu = [0] * (max_val + 1)
    mu[1] = 1

    for i in range(2, max_val + 1):
        mu[i] = 1

    for i in range(2, max_val + 1):
        if mu[i] == 1:
            for j in range(i, max_val + 1, i):
                mu[j] *= -1

            i_squared = i * i
            if i_squared <= max_val:
                for j in range(i_squared, max_val + 1, i_squared):
                    mu[j] = 0 
    
    non_coprime = 0
    
    for k in range(2, max_val + 1):
        if mu[k] == 0:
            continue 
        
        count_i = (b // k) - ((a - 1) // k)
        count_j = (d // k) - ((c - 1) // k)
        
        non_coprime += mu[k] * count_i * count_j
    

    return total_pairs + non_coprime

a, b, c, d = map(int, input().split())
print(prestej(a, b, c, d))