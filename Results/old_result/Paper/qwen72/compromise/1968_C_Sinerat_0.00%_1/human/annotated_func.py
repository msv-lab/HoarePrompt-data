#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 500 for each test case, and x_2, x_3, ..., x_n are integers such that 1 <= x_i <= 500.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the output is a list of integers `a` of length `n`, where `a[0]` is 500, and for each `1 <= i < n`, `a[i]` is the cumulative sum of `a[0]` and the elements `x[1]` to `x[i]`. The values of `t`, `n`, and `x_2, x_3, ..., x_n` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `n` and a list of integers `x` of length `n-1`. It then constructs a list `a` of length `n`, where `a[0]` is initialized to 500, and for each `1 <= i < n`, `a[i]` is the cumulative sum of `a[0]` and the elements `x[1]` to `x[i-1]`. The function prints the list `a` for each test case. The values of `t`, `n`, and `x` are not modified by the function.

