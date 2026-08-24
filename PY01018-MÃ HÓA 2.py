print("Hay dang nhap vao tro choi")
print("Hay nhap tai khoan cua ban")
print("Ten dang nhap: ")
s = input()
print("Hay nhap mat khau cua ban")
print("Mat khau: ")
m = input()
print("Hay bat dau tro choi")
print("Tro choi hom nay chung ta se choi la tinh toan")

import math

def nt(n): 
    if n < 2: return False 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return False
    return True


for t in range(int(input())): 
    s = input()
    for i in s: 
        if int(i) % 2  == 0: 
            if nt(i): 
                print("Ban da thang tro choi")
        else: 
            print("Ban da thua tro choi")