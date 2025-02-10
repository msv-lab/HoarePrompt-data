#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, k, x, and a are integers where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `k` is an input integer, `x` is an input integer, `a` is an input integer, `s` is the result of the expression `s += s // (k - 1) + 1` executed `x` times starting with `s = 1` for each of the `t` test cases, and `i` is `x - 1` for the last iteration of the inner loop in the last test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. It then calculates a value `s` by repeatedly updating `s` using the formula `s += s // (k - 1) + 1` for `x` iterations, starting with `s = 1`. Finally, it prints 'YES' if `a` is greater than or equal to `s`, otherwise it prints 'NO'. The function does not return any value; it only outputs the results for each test case.

