#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of integers of length n where -n ≤ a_i ≤ n. The input is guaranteed to have at least one valid permutation p for the given data. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: For each test case, the loop outputs a list `res` of length `n` where each element `res[i]` is calculated as `mex - ar[i]`, and `mex` is updated to `mex - ar[i]` if the new value is smaller. The final state of `res` is printed as a space-separated string for each test case. The variables `t` and `n` are consumed by the loop, and the list `a` is transformed into the output `res` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list of integers `a` of length `n`. For each test case, it computes a list `res` of the same length `n`, where each element `res[i]` is calculated as `mex - ar[i]`, and `mex` is updated to `mex - ar[i]` if the new value is smaller. The function then prints the list `res` as a space-separated string for each test case. The variables `t` and `n` are consumed, and the list `a` is transformed into the output `res` for each test case.

