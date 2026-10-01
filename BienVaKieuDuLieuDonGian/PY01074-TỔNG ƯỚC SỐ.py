import math
from array import array

N = 2000000

nt = array('i', range(N + 1))

for i in range(2, int(math.sqrt(N)) + 1):
    if nt[i] == i:
        for j in range(i * i, N + 1, i):
            if nt[j] == j:
                nt[j] = i

total = 0

for _ in range(int(input())):
    n = int(input())

    while n != 1:
        total += nt[n]
        n //= nt[n]

print(total)