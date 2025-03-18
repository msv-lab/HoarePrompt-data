#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, k, x, and a are integers for each test case where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: _ is t - 1, `k` and `a` are integers, `x` is an integer, `s` is the result of the expression `1 + sum((s // (k - 1) + 1) for _ in range(x))` after `x` iterations, `i` is `x - 1`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from the input. It then calculates a value `s` starting from 1 and iteratively updates `s` using the expression `s += s // (k - 1) + 1` for `x` iterations. Finally, it prints 'Yes' if `a` is greater than or equal to `s`, and 'No' otherwise. The function does not return any value.

