#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of integers such that -n ≤ a_i ≤ n for each test case. The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: The loop has finished executing for all test cases. For each test case, the list `p` is computed such that each element `p[i]` is equal to `mex - a[i]` where `mex` is the minimum excluded value (MEX) of the list `p` starting from `n` and updating as the loop progresses. The final value of `mex` for each test case is the smallest value in the list `p`. The list `p` is printed for each test case. The variables `t` and `n` are unchanged, and the list `a` is unchanged for each test case.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `n` and a list of integers `a`. It then computes a list `p` of the same length as `a`, where each element `p[i]` is calculated based on the minimum excluded value (MEX) of the list `p` starting from `n` and updating as the loop progresses. The final list `p` is printed for each test case. The function does not return any value; it only prints the results. The variables `t` and `n` are unchanged after the function execution, and the list `a` is also unchanged.

