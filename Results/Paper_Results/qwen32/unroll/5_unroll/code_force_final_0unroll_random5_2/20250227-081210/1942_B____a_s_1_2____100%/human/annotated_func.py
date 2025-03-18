#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n, a, p, and mex are not defined as they are re-initialized and modified for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `a` of `n` integers, and outputs a permutation `p` of the list `a` based on a specific calculation involving the minimum excluded value (mex).

