def solve(s):
    for i in s:
        if i < '0' or i > '2':
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(solve(s))