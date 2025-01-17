def check_digits(n):
    s = str(n)
    res = -1
    for i in range(len(s)):
        if int(s[i]) < 5:
            res = i
            break
    return res 
t = int(input())
for sfe in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    table = {}
    # mx = {0:[],1:0}
    ng = False
    l = 0
    r = n-1
    bsum = sum(arr)
    mx = bsum
    while (r-l != 0):
        if arr[l] <= arr[r]:
            bsum -= arr[l]
            l += 1
            mx = max(mx,bsum)
        else:
            bsum -= arr[r]
            mx = max(mx,bsum)
            r -= 1
    mx = max(0,mx)
    print(mx)
    print((sum(arr)+mx*(2**(k)-1))%(10**9+7))