#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `k` is an integer such that 2 <= k <= 30, `x` is an integer such that 1 <= x <= 100, `a` is an integer such that 1 <= a <= 10^9, `_` is `t - 1`, `s` is the result of the expression `s += s // (k - 1) + 1` executed `x` times starting from `s = 1` for each test case, `i` is `x - 1` for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `k`, `x`, and `a` within specified ranges. For each test case, it calculates a value `s` starting from 1 and iteratively updates it `x` times using the expression `s += s // (k - 1) + 1`. After the calculation, it prints 'Yes' if `a` is greater than or equal to `s`, and 'No' otherwise. The function does not return any values; it only prints the results for each test case.

