import math

n = int(input())    
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            cnt += 1

print(cnt)