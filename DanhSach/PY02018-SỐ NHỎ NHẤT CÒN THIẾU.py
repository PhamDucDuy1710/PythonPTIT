n = int(input())
a = list(map(int, input().split()))

s = set(a)

for i in range(1, n + 1):
    if i not in s:
        print(i)
        break
else: print(n + 1)