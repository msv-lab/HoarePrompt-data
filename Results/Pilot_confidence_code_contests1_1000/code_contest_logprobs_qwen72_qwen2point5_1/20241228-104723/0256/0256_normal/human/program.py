from sys import stdin

rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rint_2d = lambda n: [rint() for _ in range(n)]

n, k, p = rints()
qur, out = rint_2d(p), []
if n & 1:
    n -= 1
    k -= 1

for i in qur:
    if not (i & 1):
        out.append('X' if n - ((n - i) >> 1) > (n - k) else '.')
    elif i > n:
        out.append('X' if k > -1 else '.')
    else:
        out.append('X' if (i >> 1) >= (n - k) else '.')

print(''.join(out))
