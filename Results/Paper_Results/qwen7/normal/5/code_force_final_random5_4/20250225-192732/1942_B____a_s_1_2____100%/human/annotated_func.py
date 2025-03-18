#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: After the loop executes all iterations, `i` will be `-1`, indicating that the loop has completed all its iterations. The variable `n` will remain unchanged, holding the initial value of the input integer. The variable `mex` will be updated to the minimum value found among all elements in the list `p`. Each element `p[i]` will be equal to `mex - a[i]` for all valid indices `i`. The list `p` will have been fully modified according to the operations performed within the loop, ensuring that `mex` reflects the smallest non-negative integer not present in the list `p` as defined by the Mex function.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then constructs a permutation `p` of length `n` such that for each index `i`, `p[i]` equals `mex - a[i]`, where `mex` is the smallest non-negative integer not present in the list `p`. After constructing the permutation, it prints the elements of `p`. The function does not return any value but modifies and prints the permutation `p` for each test case.

