n = int(raw_input())
a = list(map(int, raw_input().split()))
sm = 0
m = dict()
ans = 0
for i in range(n - 1, -1, -1):
    cnt = 0
    diff = 0
    if a[i] in m:
        cnt += m[a[i]]
        diff += a[i] * m[a[i]]
    if a[i] + 1 in m:
        cnt += m[a[i] + 1]
        diff += (a[i] + 1) * m[a[i] + 1]
    if a[i] - 1 in m:
        cnt += m[a[i] - 1]
        diff += (a[i] - 1) * m[a[i] - 1]
    ans += sm - diff - a[i] * (n - i - 1 - cnt)
    sm += a[i]
    if a[i] in m:
        m[a[i]] += 1
    else:
        m[a[i]] = 1
print(ans)