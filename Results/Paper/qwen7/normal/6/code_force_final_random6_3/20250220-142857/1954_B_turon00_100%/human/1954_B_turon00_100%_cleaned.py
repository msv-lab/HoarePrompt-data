t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    tmp = a[0]
    cnt = 0
    ans = n
    for i in range(n):
        if a[i] == tmp:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
    ans = min(ans, cnt)
    if n == 1 or ans == n:
        print(-1)
    else:
        print(ans)