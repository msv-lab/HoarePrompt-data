def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
    li.sort()
    l.sort()
    if l == li:
        return 'yes'
    return 'no'
t = int(input())
for _ in range(t):
    (n, c, d) = map(int, input().split())
    l = list(map(int, input().split()))
    print(func_1(n, c, d, l))