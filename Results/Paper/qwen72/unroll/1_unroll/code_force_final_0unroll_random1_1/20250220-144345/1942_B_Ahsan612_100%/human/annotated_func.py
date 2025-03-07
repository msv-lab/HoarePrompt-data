#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 2 · 10^5) and an array a of length n, where each element a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
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
        
    #State: The loop processes each test case by reading an integer n and an array a of length n. For each test case, it calculates a new array res where each element res[i] is determined by the formula `mex - ar[i]` and updates the value of `mex` accordingly. After processing all test cases, the loop prints the resulting array res for each test case. The variables `n`, `ar`, `res`, and `mex` are reset for each new test case, and the loop continues until all test cases are processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` and an array `a` of length `n`. For each test case, it calculates a new array `res` where each element `res[i]` is determined by the formula `mex - ar[i]`, with `mex` initially set to `n` and updated during the calculation. After processing each test case, the function prints the resulting array `res`. The function does not return any value; it only prints the results. The variables `n`, `ar`, `res`, and `mex` are reset for each new test case, and the function continues processing until all test cases are handled.

