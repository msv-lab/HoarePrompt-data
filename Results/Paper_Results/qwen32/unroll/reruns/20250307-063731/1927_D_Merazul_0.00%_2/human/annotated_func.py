#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) which are the elements of the array a. The following line contains an integer q (1 ≤ q ≤ 2 · 10^5) representing the number of queries. The next q lines each contain two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of each query. The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: - After all test cases are processed, `t` will be 0 because it is decremented by 1 in each iteration of the outer loop.
    #   - The variables `k`, `a`, `b`, `f`, `m`, and `n` will be in their final states corresponding to the last test case processed.
    #   - The output for each test case is printed, but the final output state of the program is determined by the state of `t`.
    #
    #Given the loop structure and the fact that `t` is decremented until it reaches 0, the final state of `t` will be 0. The other variables (`k`, `a`, `b`, `f`, `m`, `n`) will reflect the state after processing the last test case.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array and a series of queries. For each test case, it determines if certain conditions are met based on the elements within specified ranges of the array, and outputs 'YES' or 'NO' accordingly.

