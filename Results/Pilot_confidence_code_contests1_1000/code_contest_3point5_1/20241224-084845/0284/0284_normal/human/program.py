import sys

n = int(sys.stdin.readline())
original = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())
final = map(int, sys.stdin.readline().split())

if sum(original) != sum(final):
    print('NO')
    exit(0)


def _solve(o, i, r):
    # print >> sys.stderr, i, o
    if len(o) == 1:
        return o[0]
    for k, e in enumerate(o):
        if k > 0 and o[k - 1] < e:
            r.append((i + k + 1, 'L'))
            return _solve(o[:k-1] + [o[k-1] + o[k]] + o[k+1:], i, r)
        elif k < (len(o) - 1) and e > o[k + 1]:
            r.append((i + k + 1, 'R'))
            return _solve(o[:k] + [o[k+1] + o[k]] + o[k+2:], i, r)
    print('NO')
    exit(0)

result = []

i = 0
for k, e in enumerate(final):
    j = i
    s = 0
    while e > s:
        s += original[i]
        i += 1
    if e < s:
        print('NO')
        exit(0)
    _solve(original[j:i], k, result)

print('YES')
for i, s in result:
    print('%d %s' % (i, s))
