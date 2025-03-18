#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where -n ≤ a_i ≤ n. It is guaranteed that there is at least one valid permutation p for the given data, and the sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        res = [None] * n
        
        mex = n
        
        for i in range(len(ar) - 1, -1, -1):
            res[i] = mex - ar[i]
            if mex > mex - ar[i]:
                mex = mex - ar[i]
        
        print(' '.join(str(x) for x in res))
        
    #State: _ is t-1, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `ar` is a list of integers derived from the user input, `res` is a list of `n` elements where each element `res[i]` is `mex - ar[i]` for `i` from 0 to `n-1`, `mex` is the smallest non-negative integer not present in the list `[mex - ar[i] for i in range(n)]`, and `i` is -1.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, the function computes a new list `res` of `n` elements, where each element `res[i]` is calculated as `mex - ar[i]`. Here, `mex` starts as `n` and is updated to the smallest non-negative integer not present in the list `[mex - ar[i] for i in range(n)]` during the computation. The function prints the resulting list `res` for each test case. After processing all test cases, the function completes without returning any value.

