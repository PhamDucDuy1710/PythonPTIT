def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0

for row in a:
    print(*row)