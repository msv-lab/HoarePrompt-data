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
        
    #State: After the loop executes all iterations, `t` is the input integer, `n` is the last read integer from the input, and `a` is the last read list of integers from the input. The list `p` contains the computed values for the current iteration of the loop, and it is printed. The values of `mex` are not retained between iterations.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a` from the input. It then computes a list `p` of `n` integers such that each element `p[i]` is calculated as `mex - a[i]`, where `mex` starts as `n` and is updated to the minimum of its current value and `p[i]` in each iteration. The function prints the list `p` for each test case. After all test cases are processed, the function ends.

