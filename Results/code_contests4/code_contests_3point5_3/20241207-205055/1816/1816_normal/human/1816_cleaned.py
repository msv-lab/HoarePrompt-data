(n, m) = map(int, raw_input().split())
a = map(lambda x: int(x) - 1, raw_input().split())
b = map(int, raw_input().split())
s = sum(b)
c = [0] * m
(l, r) = (0, -1)
ans = -1
t = m
while t > 0 and r + 1 < n:
    r += 1
    c[a[r]] += 1
    if c[a[r]] == b[a[r]]:
        t -= 1
if t > 0:
    print(ans)
    exit()
ans = r - l + 1 - s
while l <= r:
    c[a[l]] -= 1
    while r + 1 < n and c[a[l]] < b[a[l]]:
        r += 1
        c[a[r]] += 1
    if c[a[l]] < b[a[l]]:
        break
    l += 1
    ans = min(ans, r - l + 1 - s)
print(ans)