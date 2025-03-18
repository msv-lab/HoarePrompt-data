#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: Output State: The list `a` will contain `n` elements where each element `a[i]` (for `i` from 0 to `n-1`) is the cumulative sum of the initial value 500 and the first `i+1` elements of the list `x`. The variable `i` will have the final value of `n`, indicating that the loop has completed all its iterations.
    #
    #In more detail: After the loop has executed all its iterations, the list `a` will have been updated such that `a[0]` starts with the value 500, and each subsequent element `a[i]` (for `i` from 1 to `n-1`) will be the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the user-input list `x`. The variable `i` will have the value `n`, showing that the loop has run through all `n` iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `x` of `n-1` integers. It then computes a list `a` of length `n` where `a[0]` is initialized to 500, and each subsequent element `a[i]` is the cumulative sum of 500 and the first `i+1` elements of `x`. Finally, it prints the list `a` for each test case.

