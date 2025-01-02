(n, a) = (int(input()), [int(x) for x in stdin.readline().split()])
(tem, tem2, ans) = ([], [0] * n, 0)
for i in range(n):
    if not tem or a[i] > a[tem[-1]]:
        tem.append(i)
tem.append(n - 1)
for i in range(len(tem) - 1, 0, -1):
    cur = max(a[tem[i]], a[tem[i - 1]])
    for j in range(tem[i], tem[i - 1], -1):
        tem2[j] = cur
        cur = max(a[tem[i - 1]], cur - 1)
for i in range(n):
    ans += max(tem2[i] - a[i], 0)
print(ans)