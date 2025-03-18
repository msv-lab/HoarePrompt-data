#State of the program right berfore the function call: t is a positive integer; for each test case, n is an integer such that 2 <= n <= 2*10^5, the array a is a list of n integers where each integer a_i is in the range [1, 10^6], and q is an integer such that 1 <= q <= 2*10^5, with each query defined by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: `t` is 0, `k` is the second element of `R()` and must be greater than 0, `i` is `k`, `a` is a set containing one element from `R()`, `b` is a set containing one element from `R()`, `f` is 1, `m` is 0, `n` is 0, `u` is `True`, `v` is `False`
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a value `k`, then two sets `a` and `b` from standard input. It then iterates through numbers from 1 to `k`, checking if each number is in `a` or `b`. Based on these checks, it calculates and updates values `f`, `m`, and `n`. Finally, it prints either "YES" or "NO" based on the conditions involving `f`, `m`, and `n`.

