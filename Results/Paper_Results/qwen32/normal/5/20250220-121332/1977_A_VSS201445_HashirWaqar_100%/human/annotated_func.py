#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has finished executing all `t` iterations. For each iteration, `n` and `m` were integers read from the input, and the condition `n >= m and (n - m) % 2 == 0` was evaluated. If the condition was true, "YES" was printed; otherwise, "NO" was printed. The values of `t`, `n`, and `m` from the input remain unchanged in the context of the precondition, and no further iterations are left to execute.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`. It then checks if `n` is greater than or equal to `m` and if the difference between `n` and `m` is even. If both conditions are met, it prints "YES"; otherwise, it prints "NO". This process is repeated for all `t` test cases.

