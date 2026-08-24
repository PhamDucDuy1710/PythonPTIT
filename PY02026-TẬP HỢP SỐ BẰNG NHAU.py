n, m = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

if A == B:
    print("YES")
else:
    print("NO")