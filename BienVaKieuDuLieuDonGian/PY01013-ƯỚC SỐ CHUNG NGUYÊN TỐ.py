import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    s = sum(int(c) for c in str(g))
    print("YES" if nt(s) else "NO")