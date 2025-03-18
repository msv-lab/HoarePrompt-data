#State of the program right berfore the function call: t is a positive integer; n is an integer such that 2 <= n <= 2 * 10^5; the array a is a list of n integers where each integer is in the range [1, 10^6]; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: The output will be 'YNEOS' based on the conditions met within the loop.
#Overall this is what the function does:The function processes a series of queries on sets derived from an input list of integers. It first reads an integer `t`, indicating the number of test cases. For each test case, it reads an integer `k`, a set `a` of integers, and a set `b` of integers. It then iterates through numbers from 1 to `k`, checking membership in sets `a` and `b`. Based on these checks, it calculates values `m` and `n` and a boolean `f`. Finally, it prints 'YES' if certain conditions are met, otherwise it prints 'NO'.

