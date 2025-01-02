(n, s, f) = map(int, stdin.readline().split())
numbers = list(map(int, list(stdin.readline().strip())))
cnt = [0 for i in range(n)]
s -= 1
f -= 1
(s, f) = (min(s, f), max(s, f))
if numbers[0] == numbers[s]:
    cnt[0] = 1
for i in range(1, n):
    if numbers[i] == numbers[s]:
        cnt[i] = cnt[i - 1] + 1
    else:
        cnt[i] = cnt[i - 1]
ans = f - s
if numbers[s] != numbers[f]:
    l = -1
    r = n
    while r > l + 1:
        m = (r + l) // 2
        if cnt[m] > cnt[f]:
            r = m
        else:
            l = m
    l = -1
    r = n
    while r > l + 1:
        m = (r + l) // 2
        if cnt[m] >= cnt[f]:
            r = m
        else:
            l = m
    if r != n:
        ans = min(ans, f - r)
else:
    ans = 0
stdout.write(str(ans))