t = int(input())
for _ in range(t):
    n = int(input())
    x = [int(x) for x in input().split()]
    arr = [500] + [0]*(n-1)
    for i in range(1,n):
        arr[i] = arr[i-1] + x[i-1]
    print(*arr)