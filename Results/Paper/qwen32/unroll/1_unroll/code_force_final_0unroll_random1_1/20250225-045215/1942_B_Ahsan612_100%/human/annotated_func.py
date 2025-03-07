#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies -n <= a_i <= n. The sum of n across all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, and for each test case, a list `res` of n integers is printed where each integer `res_i` is calculated as `mex - ar_i` with `mex` starting at `n` and decreasing as the loop progresses.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it computes and prints a list `res` where each element `res_i` is calculated as `mex - ar_i`, with `mex` starting at `n` and updating based on the values in `a`.

