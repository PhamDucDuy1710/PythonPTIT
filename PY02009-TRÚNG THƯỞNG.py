for t in range(int(input())):
    cnt = [0] * 1001
    for n in range(int(input())):
        x = int(input())
        cnt[x] += 1

    ans = 1
    max_cnt = cnt[1]
    for i in range(2, 1000):
        if cnt[i] > max_cnt:
            max_cnt = cnt[i]
            ans = i
    
    print(ans)
