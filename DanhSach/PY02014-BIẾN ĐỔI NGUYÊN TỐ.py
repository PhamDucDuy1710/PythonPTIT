def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
a = list(map(int, input().split()))

ans = 0

for x in a:
    if is_prime(x):
        continue

    d = 1

    while True:
        if x - d >= 2 and is_prime(x - d):
            break

        if is_prime(x + d):
            break

        d += 1

    ans = max(ans, d)

print(ans)