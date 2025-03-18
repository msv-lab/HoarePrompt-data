#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 2 ≤ n ≤ 2·10^5, a is a list of integers where 1 ≤ a_i ≤ 10^6, q is an integer where 1 ≤ q ≤ 2·10^5, and each query (l, r) is a pair of integers where 1 ≤ l < r ≤ n. The sum of n and q across all test cases does not exceed 2·10^5.
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
        
    #State: t = 0, f = 1, m = 0, n = 0.
#Overall this is what the function does:The function `func` reads input from the user, processes a series of queries on two sets of integers, and prints a result for each query. The function does not accept any parameters directly but reads them from standard input. It processes `t` test cases, where for each test case, it reads the size `k` and two sets of integers `a` and `b`. It then checks if each integer from 1 to `k` is present in either set `a` or `b`. If all integers from 1 to `k` are present in at least one of the sets, and the counts of integers in `a` and `b` are balanced, it prints "YES"; otherwise, it prints "NO". After processing all test cases, the function leaves the program state with `t = 0`, `f = 1`, `m = 0`, and `n = 0`.

