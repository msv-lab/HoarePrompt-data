t = int(input())
 
for _ in range(t):
    n = int(input())
    
    sum, r = 0, 0
    for i in range(1, n + 1):
        if (n * (n + 1)) // 2 > i * n:
            r = i
            sum += (n * (n + 1)) // 2
        else:
            sum += i * n
 
    print(sum, n + r)
    for j in range(1, n + r + 1):
        if j <= n:
            print(1, j, end=" ")
            print(*range(1, n + 1))
        else:
            print(2, j % n, end=" ")
            print(*range(1, n + 1))