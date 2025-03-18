#State of the program right berfore the function call: The function should accept a list of integers `x` where `1 <= len(x) <= 500` and `1 <= x_i <= 500` for all `2 <= i <= n`. The function should also accept an integer `n` where `2 <= n <= 500`, and `n` is the length of the array `a` that needs to be constructed. The function should handle multiple test cases, indicated by an integer `t` where `1 <= t <= 10^4`.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The function will have processed `t` test cases, where for each test case, it constructs an array `a` of length `n` such that `a[0]` is always 500, and each subsequent element `a[i]` is the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the input list `x`. The final state of `a` for each test case is printed as a space-separated list of integers. The variables `t`, `n`, and `x` will retain their initial values as they are re-assigned in each iteration of the loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and a list of integers `x`. For each test case, it constructs an array `a` of length `n` such that `a[0]` is always 500, and each subsequent element `a[i]` (for `1 <= i < n`) is the sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the input list `x`. The final state of `a` for each test case is printed as a space-separated list of integers. The function does not return any value.

