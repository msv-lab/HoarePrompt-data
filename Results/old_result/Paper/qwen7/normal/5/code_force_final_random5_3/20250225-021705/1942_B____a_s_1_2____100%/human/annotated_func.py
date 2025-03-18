#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5. The second line of each test case contains n integers a_1, a_2, \ldots, a_n where -n ≤ a_i ≤ n, and it is guaranteed that there is at least one valid permutation p for the given data. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After the loop executes all iterations, `i` is `-1`; `mex` is the minimum value found during the loop execution among `mex - a[i]` for all `i` in the range `[0, n-1]`; `p[i]` contains the value `mex - a[i]` for each index `i` from `0` to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a list of n integers. For each test case, it calculates a permutation p of length n such that for each index i, p[i] = mex - a[i], where mex is the smallest non-negative integer not present in the modified list. The function prints the permutation p for each test case.

