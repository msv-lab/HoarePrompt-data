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
        
    #State: `t` is an input integer such that 0 < t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 2 · 10^5, `a` is a list of integers input by the user, `p` is a list of length `n` where each element `p[i]` is `mex - a[i]` for `i` from `n-1` to `0`, `mex` is the minimum value of the list `[mex, p[0], p[1], ..., p[n-1]]`, and `i` is `-1`.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers from the user. It then computes a list `p` of length `n` where each element `p[i]` is calculated as `mex - a[i]` for `i` ranging from `n-1` to `0`, with `mex` initially set to `n` and updated to the minimum of `mex` and `p[i]` during each iteration. Finally, it prints the elements of `p` for each test case. The function does not return any value.

