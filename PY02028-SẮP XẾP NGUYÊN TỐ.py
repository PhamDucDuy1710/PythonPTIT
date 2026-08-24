n = int(input())
a = list(map(int, input().split()))


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True
prime = []

for x in a:
    if is_prime(x):
        prime.append(x)
prime.sort()
j = 0

for i in range(n):
    if is_prime(a[i]):
        a[i] = prime[j]
        j += 1

print(*a)