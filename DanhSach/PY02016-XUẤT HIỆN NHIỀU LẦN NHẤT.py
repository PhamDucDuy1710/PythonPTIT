import math

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000001
    for i in a:
        cnt[i] += 1

    s = set(a)
    maxx = 0
    ans = 1
    for x in s:
        if cnt[x] > n / 2 and cnt[x] > maxx:
            maxx = cnt[x]
            ans = x
    print(ans if maxx != 0 else "NO")