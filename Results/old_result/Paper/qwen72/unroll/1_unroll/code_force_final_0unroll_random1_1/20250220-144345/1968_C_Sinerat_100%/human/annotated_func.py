#State of the program right berfore the function call: The function should take two parameters: a list `x` of integers where `1 <= x_i <= 500` and an integer `n` where `2 <= n <= 500`, and `len(x) == n - 1`. Additionally, the function should handle multiple test cases, indicated by an integer `t` where `1 <= t <= 10^4`.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the output state is a list `a` of length `n` where the first element is 1000, and each subsequent element is the sum of the previous element in `a` and the corresponding element in `x`. The values of `x` and `n` remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and a list `x` of integers. For each test case, it generates a list `a` of length `n` where the first element is 1000, and each subsequent element is the sum of the previous element in `a` and the corresponding element in `x`. The function prints the list `a` for each test case. The values of `x` and `n` remain unchanged after the function executes.

