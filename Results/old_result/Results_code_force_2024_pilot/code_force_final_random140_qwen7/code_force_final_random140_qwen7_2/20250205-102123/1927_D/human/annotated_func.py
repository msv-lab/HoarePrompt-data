#State of the program right berfore the function call: t is a positive integer; for each test case, n is an integer such that 2 <= n <= 2 * 10^5, the array a is a list of n integers where each integer is in the range [1, 10^6], and q is an integer such that 1 <= q <= 2 * 10^5. Each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `q` is 0; `l` is the return value of `R()` from the last iteration; `r` is the return value of `R()` from the last iteration; `a` is a list of integers where each element is either `j` or `i` based on the condition that `x` is not equal to `p` during each iteration; `i` is the total number of iterations performed; `j` is the value of `i` from the last iteration; `t` is 0 (since it is decremented until it reaches 0); `n` remains as the initial integer within the range \(2 \leq n \leq 2 \times 10^5\).
    #
    #Explanation: After the loop has executed all its iterations, `t` will be reduced to 0 because it starts as a positive integer and is decremented by 1 in each iteration until it reaches 0. The values of `q` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The values of `l` and `r` will be the return values of `R()` from the last iteration where the loop condition was still true. The list `a` will contain integers that are either `j` or `i` based on the condition specified, with `i` being the number of iterations performed and `j` being the value of `i` from the last iteration. The variable `n` remains unchanged as it is not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an array `a` of integers and handles a series of queries. Each query consists of two indices `l` and `r`. The function then prints the value at index `r` in the array `a` if it is greater than or equal to `l`; otherwise, it prints `-1`. The function continues processing until all test cases and queries are handled.

