t = int(input())
for _ in range(t):
    (n, c, d) = map(int, input().split())
    l = list(map(int, input().split()))
    print(func_1(n, c, d, l))

def func_1(n, c, d, l):
    l.sort()
    if not l[-1] - l[0] == (n - 1) * (c + d):
        return 'no'
    a = l[0] + l[-1]
    r = n ** 2 // 2
    if n % 2 != 0:
        if not l[r] == a // 2:
            return 'NO'
    for k in range(r):
        if not l[k] == l[-1 - k]:
            return 'no'
    return 'yes'

