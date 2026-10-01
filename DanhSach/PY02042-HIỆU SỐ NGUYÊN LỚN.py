def Sum(a, b):
    length = max(len(a), len(b))

    while len(a) < length:
        a = "0" + a

    while len(b) < length:
        b = "0" + b

    res = ""
    borrow = 0

    for i in range(length - 1, -1, -1):
        digit = int(a[i]) - int(b[i]) - borrow

        if digit < 0:
            digit += 10
            borrow = 1
        else:
            borrow = 0

        res = str(digit) + res

    res = res.lstrip('0')

    if res == "":
        res = "0"

    return res

a = input()
b = input()
aa = a.lstrip('0')
bb = b.lstrip('0')

if aa == "":
    aa = "0"

if bb == "":
    bb = "0"

if len(aa) > len(bb):
    print(Sum(aa, bb))

elif len(aa) < len(bb):
    print("-" + Sum(bb, aa))

else:
    if aa >= bb:
        print(Sum(aa, bb))
    else:
        print("-" + Sum(bb, aa))