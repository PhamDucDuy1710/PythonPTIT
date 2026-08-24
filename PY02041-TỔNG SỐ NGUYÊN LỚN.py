def Sum(a, b):
    length = max(len(a), len(b))

    while len(a) < length:
        a = "0" + a

    while len(b) < length:
        b = "0" + b

    res = ""
    remember = 0

    for i in range(length - 1, -1, -1):
        digit = int(a[i]) + int(b[i]) + remember

        remember = digit // 10

        res = str(digit % 10) + res

    if remember > 0:
        res = str(remember) + res
    res = res.lstrip('0')
    if res == "":
        res = "0"

    return res


a = input()
b = input()

print(Sum(a, b))