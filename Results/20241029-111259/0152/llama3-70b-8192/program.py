n, m, k = map(int, input().split())
x, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

ans = float('inf')
for i in range(m + 1):
    if i == m:
        t = x
    else:
        t = a[i]
    if b[i] > s:
        continue
    s_left = s - b[i]
    j = 0
    while j < k and s_left >= d[j]:
        s_left -= d[j]
        j += 1
    j -= 1
    cnt = 0
    if j != -1:
        cnt = c[j]
    ans = min(ans, (n - cnt + t - 1) // t * t)

print(ans)
