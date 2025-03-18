t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    tmp = a[0]
    aa = set(a)
    if len(aa) == 1:
        print(-1)
    cnt = 0
    ans = n
    for i in range(n):
        if a[i] == tmp:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
    ans = min(ans, cnt)
    print(ans)