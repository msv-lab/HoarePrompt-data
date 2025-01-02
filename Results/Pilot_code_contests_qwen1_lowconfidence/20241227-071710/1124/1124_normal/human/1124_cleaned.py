rints = lambda : [int(x) for x in stdin.readline().split()]
(n, m) = rints()
(ban, r, c, ans) = ([rints() for _ in range(m)], [1] * (n + 1), [1] * (n + 1), 0)
for (x, y) in ban:
    (r[x], c[y]) = (0, 0)
for i in range(2, 2 + (n - 2) // 2):
    ans += sum([r[i], r[n - i + 1], c[i], c[n - i + 1]])
if n % 2 and (r[(n + 1) // 2] or c[(n + 1) // 2]):
    ans += 1
print(ans)