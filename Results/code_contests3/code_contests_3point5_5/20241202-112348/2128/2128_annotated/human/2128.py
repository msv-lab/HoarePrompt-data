import sys
t = int(sys.stdin.readline())

for i in range(0,t):
    n,k = map(int,sys.stdin.readline().split(" "))
    arr = list(map(int,sys.stdin.readline().split()))
    arr = sorted(arr,reverse=True)
    ans = arr[0]
    if k >= n:
        k = n-1
    for l in range(1,k+1):
        ans += arr[l]
    print(ans)