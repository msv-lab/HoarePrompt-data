#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5; for each test case, a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: Output State: `t` is an integer between 1 and 10^4 inclusive. For each iteration of the loop, `n` is an integer, `a` is a list of `n` integers, and `p` is a list of `n` integers where each element is calculated based on the formula `p[i] = mex - a[i]` with `mex` being updated accordingly. After all iterations, the final state of `t`, `n`, `a`, and `p` will be as described above for each input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates a new list `p` of `n` integers based on the formula `p[i] = mex - a[i]`, where `mex` is the smallest non-negative integer not present in the list `p` so far. After processing all test cases, it outputs the list `p` for each test case.

