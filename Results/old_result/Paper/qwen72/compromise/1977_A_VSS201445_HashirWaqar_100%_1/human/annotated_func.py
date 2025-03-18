#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function should be able to handle multiple test cases, where the number of test cases `t` is a positive integer such that 1 <= t <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has completed all iterations, and for each test case, it has printed 'YES' if `n` is greater than or equal to `m` and the difference `(n - m)` is even, otherwise it has printed 'NO'. The variables `t`, `n`, and `m` are not retained after the loop, as they are re-assigned in each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `m` from the input. It then checks if `n` is greater than or equal to `m` and if the difference `(n - m)` is even. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes without retaining any of the input variables.

