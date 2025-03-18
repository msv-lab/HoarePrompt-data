#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500. The list a is now a list of n integers where a[0] = 500 and a[i] = 500 + sum(x[:i]) for 1 ≤ i < n.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `x` of `n-1` integers. It then constructs a list `a` of `n` integers where `a[0]` is 500, and each subsequent element `a[i]` (for 1 ≤ i < n) is the sum of 500 and the first `i` elements of `x`. The function prints the list `a` for each test case. The function does not return any value. After the function concludes, the input variables `t`, `n`, and `x` remain unchanged, and the list `a` is no longer accessible.

