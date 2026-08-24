import math
for t in range(int(input())):
    s = input()
    k = 0
    st = ""
    for c in s: 
        if c.isdigit(): 
            k += int(c)
        else: 
            st += c
    st = ''.join(sorted(st))
    print(st + str(k))