s = input()
n = len(s)

used = [False] * n
x = []

def Try():
    if len(x) == n:
        print("".join(x))
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            x.append(s[i])
            Try()
            x.pop()
            used[i] = False

Try()