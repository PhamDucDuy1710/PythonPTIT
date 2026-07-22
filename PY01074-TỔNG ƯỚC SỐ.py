import math

sum = 0
for t in range(int(input())):
    n = int(input())
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                sum += i
                n /= i
    
    if n != 1: sum += n

print(int(sum))