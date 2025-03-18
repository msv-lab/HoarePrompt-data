#State of the program right berfore the function call: t is a positive integer; for each test case, n is an integer such that 2 <= n <= 2 * 10^5, the array a is a list of n integers where each integer a_i is in the range 1 to 10^6, q is an integer such that 1 <= q <= 2 * 10^5, and each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: The output will be 'YNEOS' based on the conditions inside the loop.
#Overall this is what the function does:The function processes multiple test cases, each involving an array `a` and another array `b`. For each test case, it reads an integer `k`, then checks pairs of elements from `a` and `b` up to `k`. Based on specific conditions involving these elements, it determines whether to print 'Y' or 'N'. If the conditions are met, it prints 'Y'; otherwise, it prints 'N'. The function also checks additional conditions related to the counts of elements in `a` and `b` to decide the final output.

