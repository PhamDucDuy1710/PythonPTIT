def tong_chu_so(n):
    return sum(int(c) for c in str(n))


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(key=lambda x: (tong_chu_so(x), x))

    print(*a)