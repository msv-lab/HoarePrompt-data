#State of the program right berfore the function call: t is an integer where 1 \le t \le 10^4, representing the number of test cases. For each test case, n is an integer where 2 \le n \le 2 \cdot 10^5, representing the length of the array a. a is a list of n integers where 1 \le a_i \le 10^6, representing the elements of the array. q is an integer where 1 \le q \le 2 \cdot 10^5, representing the number of queries. Each query is represented by two integers l and r where 1 \le l < r \le n. The sum of n across all test cases does not exceed 2 \cdot 10^5, and the sum of q across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: t = 0, n, a, q, and the queries remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two sets of integers, `a` and `b`, and an integer `k`. It then checks if each integer from 1 to `k` is present in either `a` or `b`. If all integers from 1 to `k` are present in at least one of the sets, and the counts of unique integers in `a` and `b` are balanced (i.e., the number of integers in `a` but not in `b` and the number of integers in `b` but not in `a` are both non-negative and do not exceed `k // 2`), it prints "YES". Otherwise, it prints "NO". After processing all test cases, the function ends with `t` set to 0, and the original values of `n`, `a`, `q`, and the queries remain unchanged.

