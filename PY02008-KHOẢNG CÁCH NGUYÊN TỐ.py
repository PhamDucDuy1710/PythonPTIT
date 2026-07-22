import math 

def nt(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


prime = [0]
for i in range(2, 2000):
    if nt(i):
        prime.append(i)

n, x = map(int, input().split())


for i in range(n + 1):
    x += prime[i]
    print(x, end = ' ')