input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(raw_input())
A = map(int, input().split())
(idx, size) = (0, len(A))
total = size * (1 + size) / 2
p = [0] * size
q = [0] * size
if A[0] > 0:
    (p[0], q[0]) = (1, 0)
else:
    (q[0], p[0]) = (1, 0)
for i in xrange(1, size):
    if A[i] > 0:
        p[i] = p[i - 1] + 1
        q[i] = q[i - 1]
    else:
        p[i] = q[i - 1]
        q[i] = p[i - 1] + 1
print('%s %s' % (sum(q), sum(p)))