(n, pos, l, r) = map(int, input().split())
ans = 0
if pos < l:
    ans += l - pos
if pos > r:
    ans += pos - r
ans += min(pos - 1, n - r) + max(0, l - 1)
print(ans)