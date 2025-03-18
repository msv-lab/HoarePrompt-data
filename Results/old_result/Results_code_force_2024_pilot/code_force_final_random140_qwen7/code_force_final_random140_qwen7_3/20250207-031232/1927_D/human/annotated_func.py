#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2*10^5; a is a list of n integers where each integer a_i is such that 1 <= a_i <= 10^6; q is an integer such that 1 <= q <= 2*10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `q` is `False`; `l` is an element returned by `R()`, `r` is an element returned by `R()`, `t` is `False`, `a` is a list starting with `[1, 0]` followed by a sequence of integers where each integer represents the cumulative count of elements processed so far, `p` is the last element returned by `R()` during the loop execution, `i` is the total number of iterations performed by the loop, `j` is `(i-1, i-1)`, `x` is the last element returned by `R()` during the loop execution.
    #
    #Explanation: After the loop has executed all its iterations, the variable `t` becomes `False` because the `while t:` condition is initially true and `t` is decremented by 1 in each iteration until it reaches `False`. The variable `q` also becomes `False` because it is decremented by 1 in each iteration of the inner `while q:` loop and eventually reaches `False`. The values of `l` and `r` will be the last values returned by the function `R()` during the loop's final iteration. The list `a` will contain the cumulative counts of elements processed, starting with `[1, 0]` and continuing with a sequence of integers representing the cumulative count. The variables `p`, `i`, `j`, and `x` will retain their values from the last iteration of the loop.
#Overall this is what the function does:The function processes a list `a` of `n` integers, where each integer `a_i` is between 1 and 10^6, along with an integer `t` indicating the number of test cases, and a series of queries defined by pairs of integers `l` and `r` (where 1 <= l < r <= n). For each query, it prints either the value at index `r` in the list `a` if it meets the condition `a[r] >= l`, otherwise it prints `-1`. The function does not return any value but outputs the results directly.

