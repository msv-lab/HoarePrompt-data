from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
rints_2d = lambda n: [rints() + [i] for i in range(n)]

n = int(input())
a = sorted(rints_2d(n), key=lambda x: x[1])
out, cur = [0] * n, float('inf')

while a:
    cur, mi = min(cur - 1, a[-1][1]), [-1, float('inf')]

    for l, r, ix in a:
        if l <= cur <= r and l > mi[0]:
            mi = [l, r, ix]

    out[mi[-1]] = cur
    a.remove(mi)

print(' '.join(map(str, out)))
