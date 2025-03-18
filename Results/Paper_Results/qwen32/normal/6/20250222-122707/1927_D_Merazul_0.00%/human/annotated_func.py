#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6, q is an integer such that 1 ≤ q ≤ 2 \cdot 10^5, and for each query, l and r are integers such that 1 ≤ l < r ≤ n. The sum of n across all test cases does not exceed 2 \cdot 10^5, and the sum of q across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: t is 0, a, b, k, q, and R remain unchanged, f, m, and n are the results of the last iteration's computation.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two sets of integers `a` and `b`, and an integer `k`. For each test case, it checks if every integer from 1 to `k` is present in at least one of the sets and ensures that the counts of integers unique to each set do not exceed half of `k`. It outputs "YES" if both conditions are met, otherwise "NO".

