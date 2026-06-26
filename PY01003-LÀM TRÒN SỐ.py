for _ in range(int(input())):
    a = [int(c) for c in input().strip()]

    for i in range(len(a) - 1, 0, -1):
        if a[i] >= 5:
            a[i - 1] += 1
        a[i] = 0

    for i in range(len(a) - 1, 0, -1):
        if a[i - 1] == 10:
            a[i - 1] = 0
            if i - 1 == 0:
                a = [1] + a
            else:
                a[i - 2] += 1

    print(*a, sep="")