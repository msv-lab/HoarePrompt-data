#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies -n <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: `res` is a list of integers derived from the last test case's input, and `mex` is the minimum excluded value after processing the last test case's input.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it computes and prints a list `res` where each element is derived from the difference between a variable `mex` and the corresponding element in `a`. The variable `mex` is adjusted during the computation to ensure the conditions are met.

