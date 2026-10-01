import math

F = [0]*100
F[0], F[1] = 0, 1
for i in range(2,93):
    F[i] = F[i-1] + F[i-2]

for t in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(F[i], end = ' ')
    print()