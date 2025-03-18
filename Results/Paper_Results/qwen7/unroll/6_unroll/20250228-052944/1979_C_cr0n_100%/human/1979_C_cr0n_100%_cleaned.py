def func_1(a, b):
    return a * b // gcd(a, b)

def func_2():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = func_1(den, x)
    vprod = [den // r for r in vals]
    den = den - sum(vprod)
    if den <= 0:
        print(-1)
        return
    print(' '.join([str(x) for x in vprod]))
cases = int(input())
for n in range(cases):
    func_2()