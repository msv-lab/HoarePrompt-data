from sys import stdin, stdout

rstr = lambda: stdin.readline().strip()
rints = lambda: [int(x) for x in stdin.readline().split()]
xor = lambda x, y: sum([x[i] != y[i] for i in range(m)])
Max = 10 ** 6 + 2


def valid(x, y):
    for i in range(1, m):
        val = int(x[i - 1]) + int(x[i]) + int(y[i - 1]) + int(y[i])
        if val % 2 == 0:
            return False
    return True


n, m = rints()
mat = [rstr() for _ in range(n)]

if min(n, m) >= 4:
    print(-1)
elif min(n, m) == 1:
    print(0)
else:
    if m > n:
        mat = [[mat[j][i] for j in range(n)] for i in range(m)]
        n, m = m, n

    mem = [[Max for _ in range(8)] for _ in range(n)]
    bits = ['0' * m] + ['0' * (m - i.bit_length()) + bin(i)[2:] for i in range(1, 1 << m)]
    d = {0: [2, 5], 1: [3, 4], 2: [0, 7], 3: [1, 6], 4: [1, 6], 5: [0, 7], 6: [3, 4], 7: [2, 5]}

    if m == 2:
        d = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

    for i in range(1 << m):
        mem[0][i] = xor(bits[i], mat[0])

    for i in range(1, n):
        for j in range(1 << m):
            mem[i][j] = min(mem[i - 1][d[j][0]], mem[i - 1][d[j][1]]) + xor(mat[i], bits[j])

    print(min(mem[-1]))
