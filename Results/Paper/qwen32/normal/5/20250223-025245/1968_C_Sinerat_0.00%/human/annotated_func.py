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
        
    #State: The output state after the loop executes all the iterations is that `t` remains unchanged, `n` is the integer value of the user's input for each test case, `x` is a list of integers obtained from the user's input for each test case, and `a` is a list where each element `a[i]` (for `i` from 1 to `n - 1`) is the cumulative sum of `a[i - 1]` and `x[i - 1]`, starting with `a[0] = 500`. The loop processes each test case independently, and for each test case, it prints the list `a`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it constructs a list `a` of length `n` starting with `a[0] = 500`. Each subsequent element `a[i]` is the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the input list `x`. It then prints the list `a` for each test case.

