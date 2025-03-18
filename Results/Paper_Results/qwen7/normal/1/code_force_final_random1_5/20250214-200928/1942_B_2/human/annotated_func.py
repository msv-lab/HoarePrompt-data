#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the array a is a list of n integers where -n ≤ a_i ≤ n.
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
        
    #State: After all iterations of the loop, `i` will be `-1`, `mex` will be `mex - len(ar)*ar[-1] + sum(ar)`, and `res` will be a list of length `n` where each element is `mex - ar[i]` for the corresponding index `i` from `-1` to `n-1`
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then computes a new list `res` of length `n` where each element is calculated as `mex - a[i]`, with `mex` being the smallest non-negative integer not present in the list `a`. Finally, it prints the elements of `res` separated by spaces.

