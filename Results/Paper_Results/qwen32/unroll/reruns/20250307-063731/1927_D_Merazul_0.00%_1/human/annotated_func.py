#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 · 10^5; a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6; q is an integer such that 1 ≤ q ≤ 2 · 10^5; for each query, l and r are integers such that 1 ≤ l < r ≤ n.
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
        
    #State: the printed characters 'YES' or 'NO' for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it determines if a certain condition is met based on the presence of integers in two sets and prints 'YES' or 'NO' accordingly.

