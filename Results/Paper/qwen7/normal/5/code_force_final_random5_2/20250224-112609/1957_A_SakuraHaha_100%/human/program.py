def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
    for x in cnt.values():
        ans += x // 3
    print(ans)
 
t = 1
t = int(input())
for _ in range(t):
    solve()