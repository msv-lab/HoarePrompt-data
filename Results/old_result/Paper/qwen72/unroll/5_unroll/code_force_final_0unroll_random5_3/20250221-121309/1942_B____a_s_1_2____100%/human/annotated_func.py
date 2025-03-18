#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of integers such that -n ≤ a_i ≤ n for each 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
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
        
    #State: After all iterations of the loop, `t` is the same input integer, `n` is the last input integer for the final iteration, and `a` is the last list of integers input for the final iteration. The list `p` will contain the calculated values for the final iteration, and `mex` will be the minimum value in `p` for the final iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates a permutation `p` of length `n` such that each element `p[i]` is determined by the formula `mex - a[i]`, where `mex` starts at `n` and is updated to the minimum value between `mex` and `p[i]` for each `i` in reverse order. After processing all test cases, the function prints the permutation `p` for each test case. The final state of the program is that `t` remains the same, `n` is the last input integer for the final test case, and `a` is the last list of integers input for the final test case. The list `p` will contain the calculated permutation for the final test case, and `mex` will be the minimum value in `p` for the final test case.

