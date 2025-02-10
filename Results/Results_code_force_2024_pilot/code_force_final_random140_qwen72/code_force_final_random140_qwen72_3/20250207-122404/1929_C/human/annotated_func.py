#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each of the t test cases, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: After the loop executes all the iterations, `t` is 0, and for each of the `t` test cases, `k`, `x`, and `a` retain their initial values from the input. The variable `s` is the final value after `x` iterations of the inner loop for each test case, and `i` is `x - 1` for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. It then calculates a value `s` based on `k` and `x` through a series of iterations. Finally, it prints 'YES' if `a` is greater than or equal to `s`, otherwise it prints 'NO'. The function does not return any value; it only prints the result for each test case. After the function completes, `t` is effectively 0 (as all test cases have been processed), and the values of `k`, `x`, and `a` for each test case are no longer relevant.

