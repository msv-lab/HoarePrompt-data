(n, m) = map(int, stdin.readline().split())
(edges, cur) = ([], 0)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if not m:
            break
        if gcd(i, j) == 1:
            m -= 1
            edges.append('%d %d' % (i, j))
            cur = max(cur, j)
if m or cur != n:
    print('Impossible')
else:
    print('%s\n%s' % ('Possible', '\n'.join(edges)))