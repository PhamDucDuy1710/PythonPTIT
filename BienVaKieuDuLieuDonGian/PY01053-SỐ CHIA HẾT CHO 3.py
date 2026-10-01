for t in range(int(input())):
    n = sum(int(i) for i in input())
    print("YES" if n % 3 == 0 else "NO")