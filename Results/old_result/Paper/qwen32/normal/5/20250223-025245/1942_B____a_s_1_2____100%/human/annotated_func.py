#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies -n <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: After all iterations, `t` will be 0, and for each test case, `p` will be a list of integers where each element `p[i]` is calculated as `mex - a[i]` from the end of the list `a` to the beginning, with `mex` being updated to the minimum of its current value and `p[i]` at each step. The final `mex` represents the smallest non-negative integer not present in the list `p`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it computes and prints a list `p` where each element `p[i]` is determined by subtracting the corresponding element `a[i]` from a value `mex` that is updated to ensure `p` is a valid permutation.

