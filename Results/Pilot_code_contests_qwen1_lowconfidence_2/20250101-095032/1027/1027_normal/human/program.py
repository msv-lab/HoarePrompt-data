n, m = map(int, raw_input().split())
count = [0] * n
for i in xrange(m):
    a, b = map(int, raw_input().split())
    count[a - 1] += 1
    count[b - 1] += 1
for i in xrange(n):
    print(count[i])
