#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers with 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `_` is `t - 1`, `k` is an input integer, `x` is an input integer, `a` is an input integer, `i` is `x - 1`, `s` is the final value after `x` iterations of the inner loop, where the value of `s` depends on `k` and `x`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, and for each test case, it reads three integers `k`, `x`, and `a`. It then calculates a value `s` based on `k` and `x` through an iterative process. After the calculation, it prints 'Yes' if `a` is greater than or equal to `s`, and 'No' otherwise. The function does not return any value. After the function concludes, `t` test cases have been processed, and for each test case, a result ('Yes' or 'No') has been printed based on the comparison of `a` with the calculated `s`.

