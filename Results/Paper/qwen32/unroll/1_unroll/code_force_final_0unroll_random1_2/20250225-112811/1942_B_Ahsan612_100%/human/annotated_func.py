#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        res = [None] * n
        
        mex = n
        
        for i in range(len(ar) - 1, -1, -1):
            res[i] = mex - ar[i]
            if mex > mex - ar[i]:
                mex = mex - ar[i]
        
        print(' '.join(str(x) for x in res))
        
    #State: For each test case, a list `res` of n integers is printed where each element `res[i]` is calculated as `mex - ar[i]` starting from the end of the list `ar` to the beginning. The variable `mex` is initially set to `n` and is updated to the minimum value of `mex - ar[i]` encountered during the iteration. The state of `t`, `n`, and `ar` from the initial state remains unchanged except that `ar` is processed to produce `res`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `a` of `n` integers, then computes and prints a list `res` of `n` integers where each element `res[i]` is determined by subtracting the corresponding element `a[i]` from a variable `mex` initialized to `n`, updating `mex` to the minimum value encountered during the computation.

