n = int(input())

a = []

while len(a) < n:
    a.extend(map(int, input().split()))

chan = []
le = []

for x in a:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

chan.sort()
le.sort(reverse=True)

i = 0
j = 0

for k in range(n):
    if a[k] % 2 == 0:
        a[k] = chan[i]
        i += 1
    else:
        a[k] = le[j]
        j += 1

print(*a)