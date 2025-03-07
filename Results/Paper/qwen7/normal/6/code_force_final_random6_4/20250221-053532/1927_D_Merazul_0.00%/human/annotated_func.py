#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that 1 ≤ a_i ≤ 10^6; q is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers l and r such that 1 ≤ l < r ≤ n.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        *_, k = R()
        
        a = {*R()}
        
        b = {*R()}
        
        f = 1
        
        m = n = k // 2
        
        for i in range(1, k + 1):
            u = i in a
            v = i in b
            f &= u | v
            m -= u & ~v
            n -= ~u & v
        
        print('YNEOS'[f ^ 1 or m | n < 0::2])
        
    #State: After the loop executes all iterations, `f` will be `True` if there exists at least one `i` such that `i` is in both `a` and `b`, or in exactly one of them. `m` and `n` will both be `0` because they are decremented each time `i` is in `a` but not in `b`, or in `b` but not in `a`, respectively. The values of `u` and `v` will reflect the membership of `k` in sets `a` and `b`, respectively.
#Overall this is what the function does:The function processes a series of queries on two sets of integers, `a` and `b`. For each query defined by integers `l` and `r`, it checks if there exists at least one integer within the range `[l, r]` that is present in both sets `a` and `b`, or in exactly one of them. If such an integer exists, it prints "YES"; otherwise, it prints "NO". The function also ensures that `m` and `n` are both set to zero by decrementing them whenever an integer is found in one set but not the other.

