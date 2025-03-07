def rem_p(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x<= n)
    return n
    
def solve():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        p = list(map(int, input().split()))
        qs = list(map(int, input().split()))
        
        res = []
        for n in qs:
            res.append(rem_p(n, p))
            print(' '.join(map(str, res)))
            
solve()