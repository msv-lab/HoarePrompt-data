input = sys.stdin.readline
(n, k) = map(int, input().split())
(a, b, c, d) = map(int, input().split())
if n == 4:
    print('-1')
elif k >= n + 1:
    chain = [a, c]
    for i in range(1, n + 1):
        if i not in [a, b, c, d]:
            chain.append(i)
    chain.append(b)
    chain.append(d)
    p1 = list(chain)
    (p1[-1], p1[-2]) = (p1[-2], p1[-1])
    print(' '.join(map(str, p1)))
    p2 = list(chain)
    (p2[0], p2[1]) = (p2[1], p2[0])
    print(' '.join(map(str, p2)))
else:
    print('-1')