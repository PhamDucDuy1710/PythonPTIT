import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

for t in range(int(input())):
    s = input()
    x = int(s[:3])
    y = int(s[-3::])
    print("YES" if nt(x) and nt(y) else "NO") 