#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
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
        
    #State: t is an input integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data. For each test case, p is a list of n integers where each p_i is calculated as p[i] = mex - a[i] and mex is updated to be the minimum of mex and p[i], starting with mex = n. The final values of p for each test case are printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then computes a list `p` of `n` integers where each element `p[i]` is calculated as `mex - a[i]`, with `mex` initially set to `n` and updated to the minimum of `mex` and `p[i]` in each iteration. The function prints the final values of `p` for each test case.

