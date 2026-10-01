import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    matrix = []
    idx = 1
    for i in range(n):
        row = [int(x) for x in data[idx : idx + n]]
        matrix.append(row)
        idx += n
    k = int(data[idx])
    sum_upper = 0
    sum_lower = 0 
    
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                sum_upper += matrix[i][j]
            elif i + j > n - 1:
                sum_lower += matrix[i][j]
                
    diff = abs(sum_upper - sum_lower)
    
    if diff <= k:
        print("YES")
    else:
        print("NO")
        
    print(diff)

if __name__ == "__main__":
    main()