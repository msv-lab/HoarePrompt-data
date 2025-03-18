#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the array a is a list of n integers where -n ≤ a_i ≤ n. It is guaranteed that there is at least one valid permutation p for the given data, and the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After executing the loop for `t` times, the variable `p` will contain an array of integers for each iteration, where each element `p[i]` is calculated as `mex - a[i]` and `mex` is updated to be the minimum of itself and `p[i]` during each iteration. The final state of `p` for each iteration is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (size of the array), and an array `a` of `n` integers. It then calculates a valid permutation `p` for the given array `a`, where each element `p[i]` is determined as `mex - a[i]` and `mex` is updated to be the minimum of itself and `p[i]` during each iteration. Finally, it prints the resulting permutation `p` for each test case.

