#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
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
        
    #State: For each test case, the loop outputs a list `res` of n integers where each element is calculated as `mex - ar[i]` starting from the end of the list `ar` and updating `mex` accordingly. The final state of `t` is 0, as all test cases have been processed. The variables `n` and `a` (or `ar`) are reset for each test case, and their final state is undefined after the last test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `ar` of `n` integers. It then computes a new list `res` of `n` integers where each element is calculated as `mex - ar[i]` starting from the end of the list `ar`, and updates `mex` accordingly. The function prints the resulting list `res` for each test case. After processing all test cases, the function concludes, and the state of `t`, `n`, and `ar` is undefined.

