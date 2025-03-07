#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where each element x_i satisfies 1 <= x_i <= 500. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, `a` is a list with `n` elements where `a[0]` is 500 and each subsequent element `a[i]` for `1 <= i < n` is the cumulative sum of the first `i` elements of `x` starting from 500. The loop has processed all `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it constructs a list `a` of length `n` such that the first element is 500 and each subsequent element is the cumulative sum of the previous element and the corresponding element from the input list `x`. The function prints this list `a` for each test case.

