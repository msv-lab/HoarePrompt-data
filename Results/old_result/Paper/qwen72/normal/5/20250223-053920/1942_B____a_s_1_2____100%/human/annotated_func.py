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
        
    #State: After all iterations of the loop, the variable `t` will be 0 (since the loop has completed all its iterations), and for each test case, the list `p` will contain a permutation of integers from 0 to n-1, where `p[i]` is calculated as `mex - a[i]` and `mex` is updated to be the minimum of `mex` and `p[i]` in each iteration. The final value of `n` and the list `a` will remain unchanged for each test case, but they will be re-assigned in each iteration of the outer loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates a permutation `p` of integers from 0 to `n-1` based on the values in `a` and a variable `mex` initialized to `n`. The function prints the calculated permutation `p` for each test case. After processing all test cases, the function does not return any value, and the variables `t`, `n`, and `a` are no longer in scope. The final state of the program is that the input has been processed, and the permutations have been printed to the standard output.

