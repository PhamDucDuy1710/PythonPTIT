n = int(input())

tren = 0
duoi = 0

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if i < j:
            tren += a[j]
        elif i > j:
            duoi += a[j]

k = int(input())

diff = abs(tren - duoi)

print("YES" if diff <= k else "NO")
print(diff)