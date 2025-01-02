n = int(raw_input())
a = map(int, raw_input().split())

d = [0] * 5000
for i in xrange(n):
    for j in xrange(i+1, n):
        d[a[j]-a[i]] += 1

c = [0] * 5000
for i in xrange(1, 5000):
    c[i] = c[i-1] + d[i]

ans, m = 0.0, float(sum(d))
for i in xrange(4999, 0, -1):
    if d[i] == 0:
        continue
    for j in xrange(i):
        ans += (d[i] / m) * (d[j] / m) * (c[i-j-1] / m)

print("{0:.10f}".format(ans))
