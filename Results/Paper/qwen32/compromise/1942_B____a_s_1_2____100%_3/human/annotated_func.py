#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies -n <= a_i <= n. The sum of n across all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: The loop has executed `t` times. For each execution, `n` is an integer such that 1 <= n <= 2 * 10^5, `a` is a list of `n` integers where each element `a_i` satisfies -n <= a_i <= n. The list `p` is computed such that `p[i] = mex - a[i]` for each `i` from `n-1` to `0`, where `mex` starts at `n` and is updated to be the minimum value in `p` after each assignment. After all `t` iterations, the final output consists of `t` lines, each line representing the list `p` computed for the corresponding input values of `n` and `a`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it computes and outputs a list `p` of `n` integers based on the input list `a`. The list `p` is constructed such that for each element `i` from `n-1` to `0`, `p[i]` is calculated as `mex - a[i]`, where `mex` is initially `n` and is updated to the minimum value in `p` after each assignment. The function outputs `t` lines, each representing the list `p` for the corresponding input values of `n` and `a`.

