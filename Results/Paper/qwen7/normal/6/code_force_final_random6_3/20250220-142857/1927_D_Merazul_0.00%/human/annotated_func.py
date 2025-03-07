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
        
    #State: Output State: `f` is True if every integer `i` from 1 to `k` is found in either set `a` or set `b`, otherwise `f` is False. `i` is `k + 1`, `b` is a set containing all elements of the tuple returned by `R()`, `v` is a boolean indicating whether `i` is in `b`, `u` is a boolean indicating whether `i` is in `a`, `m` is `k // 2 - sum((u & ~v) for i in range(1, k + 1))`, `n` is `k // 2 - sum((~u & v) for i in range(1, k + 1))`.
    #
    #After the loop executes all its iterations, the final state of the variables can be described as follows:
    #- The variable `f` will be `True` if and only if every integer `i` from 1 to `k` is present in at least one of the sets `a` or `b`. Otherwise, `f` will be `False`.
    #- The variable `i` will be equal to `k + 1` because the loop increments `i` from 1 to `k` and then exits.
    #- The set `b` will contain all elements of the tuple returned by `R()` after the loop has completed.
    #- The boolean `v` will indicate whether `i` (which is now `k + 1`) is in `b`, but since `i` exceeds the range of `b`, `v` will be `False`.
    #- The boolean `u` will indicate whether `i` (which is now `k + 1`) is in `a`, but since `i` exceeds the range of `a`, `u` will be `False`.
    #- The variable `m` will be calculated as `k // 2 - sum((u & ~v) for i in range(1, k + 1))`. Since `i` exceeds the range of both `a` and `b`, `u & ~v` will be `False` for all iterations, making `m` equal to `k // 2`.
    #- The variable `n` will be calculated as `k // 2 - sum((~u & v) for i in range(1, k + 1))`. Similarly, since `i` exceeds the range of both `a` and `b`, `~u & v` will be `False` for all iterations, making `n` equal to `k // 2`.
#Overall this is what the function does:The function processes a series of queries on sets derived from input data. For each query, it checks if every integer from 1 to k (where k is provided for each query) is present in at least one of two sets, a and b. If every integer from 1 to k is found in either set, it sets a flag `f` to True; otherwise, it sets `f` to False. After processing all queries, it prints 'YES' if `f` is True for all queries, and 'NO' if `f` is False for any query.

