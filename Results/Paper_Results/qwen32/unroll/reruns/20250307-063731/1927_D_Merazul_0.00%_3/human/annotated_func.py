#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, it starts with an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the array a. This is followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. Next, an integer q (1 ≤ q ≤ 2 · 10^5) is given, representing the number of queries. Each of the next q lines contains two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of the query. The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: A series of 'Y' or 'NO' strings, one for each test case, indicating whether the conditions are met for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array and a series of queries. For each test case, it checks if certain conditions are met based on the elements of two sets derived from the input and prints 'YES' or 'NO' accordingly.

