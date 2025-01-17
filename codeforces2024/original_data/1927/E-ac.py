def solve():
    n, k = map(int, input().split())
    l, r = 1, n
    ans = [0] * n
    for i in range(k):
        for j in range(i, n, k):
            if i % 2 == 0:
                ans[j] = l
                l += 1
            else:
                ans[j] = r
                r -= 1
    print(*ans)
    
    
for _ in range(int(input())):
    solve()