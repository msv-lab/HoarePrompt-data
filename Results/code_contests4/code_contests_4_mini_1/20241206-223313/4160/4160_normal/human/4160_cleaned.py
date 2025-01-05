add = lambda a, b: (a + b) % mod
mult = lambda a, b: a % mod * (b % mod) % mod
rints = lambda : [int(x) for x in stdin.readline().split()]
(n, m, b, mod) = rints()
(a, mem) = (rints(), [[[int(j == 0) for _ in range(b + 1)] for j in range(m + 1)] for _ in range(2)])
ans = 0
for i in range(1, n + 1):
    ix = i & 1
    for j in range(1, m + 1):
        for k in range(a[i - 1], b + 1):
            mem[ix][j][k] = mem[ix ^ 1][j][k]
            mem[ix][j][k] = add(mem[ix][j][k], mem[ix][j - 1][k - a[i - 1]])
for i in range(b + 1):
    ans = add(ans, mem[n & 1][m][i])
print(ans)