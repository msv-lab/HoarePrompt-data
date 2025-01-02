rints = lambda : [int(x) for x in stdin.readline().split()]
(n, k) = rints()
(a, ans, s) = (rints(), [], 0)
for i in range(1, n):
    if s - (n - i - len(ans) - 1) * a[i] * (i - len(ans)) < k:
        ans.append(i + 1)
        n -= 1
    else:
        s += a[i] * (i - len(ans))
print('\n'.join(map(str, ans)))