from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)
 
def solve():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    den = vals[0]
    for x in vals:
        den = lcm(den, x)
    # prod = 1
    # for r in vals:
    #     prod *= r
    vprod = [den//r for r in vals]
    den = den - sum(vprod)
    if den <= 0:
        print(-1)
        return
    
    print(" ".join([str(x) for x in vprod]))
 
cases = int(input())
for n in range(cases):
    solve()