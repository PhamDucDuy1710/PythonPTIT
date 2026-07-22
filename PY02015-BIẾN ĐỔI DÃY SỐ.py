def step(a):
    return [
        abs(a[0] - a[1]),
        abs(a[1] - a[2]),
        abs(a[2] - a[3]),
        abs(a[3] - a[0])
    ]

while True:
    a = list(map(int, input().split()))
    if a == [0,0,0,0]:
        break

    cnt = 0
    while not(a[0] == a[1] == a[2] == a[3]):
        a = step(a)
        cnt += 1
    print(cnt)