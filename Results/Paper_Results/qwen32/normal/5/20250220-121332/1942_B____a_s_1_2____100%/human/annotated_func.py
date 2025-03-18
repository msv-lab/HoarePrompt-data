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
        
    #State: t is 0, n is undefined, a is undefined, p is undefined, mex is undefined.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then computes and prints a permutation `p` of the list `a` such that for each element in `p`, the value is determined by subtracting the corresponding element in `a` from a decreasing maximum value `mex`. The final state of the program is that it has processed all test cases and printed the required permutations.

