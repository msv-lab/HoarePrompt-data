#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: After the loop executes all the iterations, `i` is `-1`, `ar` is a list of integers, `n` is the input integer, `mex` is equal to `n - sum(ar)`, and `res` is a list of length `n` where each element `res[i]` is equal to `mex - ar[i]` if `mex > mex - ar[i]`, otherwise `res[i]` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `ar`. For each test case, it computes a new list `res` where each element `res[i]` is calculated based on the maximum excluded number (`mex`) and the corresponding element in `ar`. Specifically, `res[i]` is set to `mex - ar[i]` if `mex > mex - ar[i]`, otherwise `res[i]` remains unchanged. Finally, it prints the elements of `res` for each test case.

