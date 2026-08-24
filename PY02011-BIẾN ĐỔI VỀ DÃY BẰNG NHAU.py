n = int(input())
a = list(map(int, input().split()))

min_step = float('inf')
ans = 0

for x in a:
    step = 0

    for y in a:
        step += abs(y - x)

    if step < min_step:
        min_step = step
        ans = x

print(min_step, ans)