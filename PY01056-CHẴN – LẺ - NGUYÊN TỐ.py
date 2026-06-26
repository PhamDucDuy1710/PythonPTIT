import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    tong = 0
    for i in range(len(s)):
        x = int(s[i])
        tong += x
        if (i + 1) % 2 == 1:      
            if x % 2 == 0:
                return "NO"
        else:                     
            if x % 2 == 1:
                return "NO"
    return "YES" if nt(tong) else "NO"

for _ in range(int(input())):
    print(solve(input()))