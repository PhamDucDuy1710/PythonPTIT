import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(s):
    if(not nt(len(s))): 
        return "NO"
    cnt = 0
    for i in s:
        n = int(i)
        if(nt(n)):
            cnt += 1
    if cnt > len(s) - cnt:
        return "YES"
    else:
        return "NO"


for t in range(int(input())):
    s = input()
    print(solve(s))