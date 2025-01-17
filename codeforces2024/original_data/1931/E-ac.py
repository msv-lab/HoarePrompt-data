t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(str,input().split()))
    len_arr = [0]*n
    zrr = [0]*n
    ans = 0
    for i in range(n):
        len_arr[i] = len(a[i])
        zrr[i] = len(a[i]) - len(a[i].rstrip("0"))
        ans += len_arr[i] - zrr[i]
    zrr.sort(reverse=True)
    for i in range(n):
        if i %2 != 0:
            ans += zrr[i]
    if ans - 1>= m:
        print("Sasha")
    else:
        print("Anna")