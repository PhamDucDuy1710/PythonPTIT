def solve(s):
    if len(s) < 3:
        return "NO"
    up = True
    a = list(int(i) for i in s)
    for i in range(1,len(s)):
        if up and a[i] <= a[i-1]:
            up = False
        elif not up and a[i] >= a[i-1]:
            return "NO"
    return "YES"
for t in range(int(input())):
    s = input()
    print(solve(s))