#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; n is an integer where 2 ≤ n ≤ 2 · 10^5; a is a list of n integers where 1 ≤ a_i ≤ 10^6; q is an integer where 1 ≤ q ≤ 2 · 10^5; l and r are integers for each query where 1 ≤ l < r ≤ n.
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
        
    #State: After all iterations of the loop, `t` will be 0, `i` will be the length of the iterable returned by `R()`, `a` will be a list containing the sequence of values that `j` took during each iteration, `p` will be the last element from the iterable returned by `R()`, `j` will be the last value of `i` or the second-to-last value of `i` depending on whether the last element of `R()` was different from the second-to-last element, `q` will be 0, `n` will remain unchanged, and `l` and `r` will be the last values read from the queries.
#Overall this is what the function does:The function reads multiple sets of inputs and processes queries on a constructed list. It accepts no explicit parameters but reads from standard input. For each test case defined by `t`, it constructs a list `a` based on the input values and processes `q` queries. Each query consists of two integers `l` and `r`, and the function prints either the value of `a[r]` if it is greater than or equal to `l`, or `-1` otherwise. After processing all queries for all test cases, the function terminates with `t` and `q` set to 0, and the final state of `a` reflects the constructed list for the last test case.

