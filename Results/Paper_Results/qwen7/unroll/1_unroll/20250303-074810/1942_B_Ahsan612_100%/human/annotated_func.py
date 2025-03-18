#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5; for each test case, a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5; for each test case, ar is a list of n integers such that -n ≤ a_i ≤ n; for each test case, res is a list of n integers representing the result of the loop, where each element res[i] is calculated as mex - ar[i] with mex being decremented accordingly from n to 0 as the loop iterates backwards through ar.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `ar` of `n` integers. It then calculates a new list `res` where each element `res[i]` is determined as `mex - ar[i]`, with `mex` being decremented based on the values in `ar`. Finally, it prints the elements of `res` for each test case.

