#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) and a list of integers a_1, a_2, ..., a_n (-n ≤ a_i ≤ n), where n is the length of both p and a, and a is constructed based on the MEX operation on p. It is guaranteed that there is at least one valid permutation p for the given data, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `_` is `t - 1`, `n` is an input integer, `ar` is a list of integers provided by the user input, `res` is a list of `n` elements where each element `res[i]` is equal to `mex - ar[i]` for each `i` from `0` to `n-1`, and `mex` is the smallest non-negative integer that is not present in the list `ar` after all iterations. The variable `i` is `-1` after the loop has completed all its iterations.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it takes an integer `n` and a list of integers `ar` of length `n`. It then computes a new list `res` of the same length, where each element `res[i]` is calculated as `mex - ar[i]`, with `mex` initially set to `n` and updated during the computation. The function prints the resulting list `res` for each test case. After processing all test cases, the function terminates without returning any value.

