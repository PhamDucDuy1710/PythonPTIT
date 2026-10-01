t = int(input())

for _ in range(t):
    S = input().strip()
    N = input().strip()
    
    cnt = 0
    i = 0
    n = len(N)
    
    while i <= len(S) - n:
        if S[i:i+n] == N:
            cnt += 1
            i += n  
        else:
            i += 1
    
    print(cnt)