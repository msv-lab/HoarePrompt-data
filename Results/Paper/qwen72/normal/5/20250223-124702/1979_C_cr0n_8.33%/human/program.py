def solve():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
    vprod = [prod//r for r in vals]
    den = prod - sum(vprod)
    if den <= 0:
        print(-1)
        return
    
    print(" ".join([str(x) for x in vprod]))
 
cases = int(input())
for n in range(cases):
    solve()