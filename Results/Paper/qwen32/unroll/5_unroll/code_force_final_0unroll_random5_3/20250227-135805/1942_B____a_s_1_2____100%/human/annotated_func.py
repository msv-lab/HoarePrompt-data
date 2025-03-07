#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies -n <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: For each of the t test cases, a permutation p of length n is printed where each element p[i] is calculated as mex - a[i] starting from i = n-1 to i = 0, and mex is updated to be the minimum of its current value and p[i]. The value of t, n, and the list a remain unchanged across different test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints a permutation `p` of length `n` for each test case, where each element `p[i]` is determined by the formula `mex - a[i]`, starting from `i = n-1` to `i = 0`, and `mex` is updated to be the minimum of its current value and `p[i]`. The values of `t`, `n`, and the list `a` remain unchanged across different test cases.

