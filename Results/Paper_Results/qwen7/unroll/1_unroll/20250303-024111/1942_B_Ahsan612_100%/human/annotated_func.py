#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where -n ≤ a_i ≤ n for all 1 ≤ i ≤ n.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and res is a list of n integers representing the result of the loop operations, where each element res[i] is calculated as mex - ar[i] and mex is decremented accordingly during the loop execution.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `ar` of `n` integers. It then calculates a list `res` of length `n`, where each element `res[i]` is computed as `mex - ar[i]`, with `mex` being decremented during the calculation. Finally, it prints the list `res` for each test case.

