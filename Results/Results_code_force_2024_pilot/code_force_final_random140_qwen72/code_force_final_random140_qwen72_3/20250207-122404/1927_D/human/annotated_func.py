#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 2·10^5, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^6. q is an integer where 1 ≤ q ≤ 2·10^5, representing the number of queries. Each query is represented by two integers l and r where 1 ≤ l < r ≤ n. The sum of n and q across all test cases does not exceed 2·10^5.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        R()
        
        a = [0]
        
        p = i = j = 0
        
        for x in R():
            j = (j, i)[x != p]
            a += j,
            p = x
            i += 1
        
        q, = R()
        
        while q:
            q -= 1
            l, r = R()
            print(*((a[r], r), [-1] * 2)[a[r] < l])
        
    #State: `t` is 0, `n` is an integer where 2 ≤ n ≤ 2·10^5, `a` is a list of length `n` starting with `[0]` followed by the sequence of indices where `x` was different from `p`, `i` is `n`, `j` is 0, `l` is the last element from `R()` before the loop ends, `r` is the second-to-last element from `R()` before the loop ends, `p` is the last element of the iterable returned by `R()`, `q` is 0.
#Overall this is what the function does:The function processes multiple test cases, each involving an array and a set of queries. For each test case, it reads the array and constructs a new list `a` that tracks the positions where the elements change. For each query, it prints the result based on the constructed list `a` and the query parameters. After processing all test cases, the function ensures that all input has been read and processed, and the state variables related to the current test case are reset or exhausted.

