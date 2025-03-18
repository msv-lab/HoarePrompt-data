def func_1(n, p):
    while n >= min(p):
        n -= sum((1 for x in p if x <= n))
    return n

def func_2():
    t = int(input())
    for _ in range(t):
        (k, q) = map(int, input().split())
        p = list(map(int, input().split()))
        qs = list(map(int, input().split()))
        res = []
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
func_2()