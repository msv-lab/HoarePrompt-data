from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, a, b, mem = int(input()), rints(), rints(), [[0 for _ in range(6)] for _ in range(2)]
ans = 0

for i in range(n):
    mem[0][a[i]] += 1
    mem[1][b[i]] += 1

for i in range(1, 6):
    if (mem[0][i] + mem[1][i]) & 1:
        ans = -1
        break

    ans += max((mem[0][i] - mem[1][i]) // 2, 0)

print(ans)
