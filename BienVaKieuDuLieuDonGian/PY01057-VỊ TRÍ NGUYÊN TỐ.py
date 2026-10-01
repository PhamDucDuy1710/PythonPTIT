import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

def solve(s):
    for i in range(len(s)):
        if nt(i):
            if not nt(int(s[i])):
                return "NO"
        else:
            if nt(int(s[i])):
                return "NO"
    return "YES"

for t in range(int(input())):
    print(solve(input()))
