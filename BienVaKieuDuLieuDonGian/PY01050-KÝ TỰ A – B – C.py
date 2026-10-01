def Try(s, n):
    if len(s) == n:
        a = s.count('A')
        b = s.count('B')
        c = s.count('C')
        if a > 0 and b > 0 and c > 0 and a <= b <= c:
            print(s)
        return

    for ch in ['A', 'B', 'C']:
        Try(s + ch, n)

N = int(input())

for i in range(3, N + 1):
    Try("", i)