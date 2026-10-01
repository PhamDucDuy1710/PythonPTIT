n, k = map(int, input().split())

se = set(map(int, input().split()))
c = sorted(se)
n = len(c)

a = [0] * (k + 1)

def result():
    for i in range(1, k + 1):
        print(c[a[i] - 1], end=" ")
    print()

def Try(m):
    for i in range(a[m - 1] + 1, n - k + m + 1):
        a[m] = i
        if m == k:
            result()
        else:
            Try(m + 1)

Try(1)