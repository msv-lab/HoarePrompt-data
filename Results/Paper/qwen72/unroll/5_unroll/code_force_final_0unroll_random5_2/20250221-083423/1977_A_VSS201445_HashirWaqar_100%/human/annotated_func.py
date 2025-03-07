#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, where `n` and `m` are integers such that 1 ≤ n, m ≤ 100. The function should be able to handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop executes for `t` iterations, where `t` is the number of test cases. For each iteration, it reads a pair of integers `n` and `m` from the input. If `n` is greater than or equal to `m` and the difference `(n - m)` is even, it prints 'YES'. Otherwise, it prints 'NO'. The values of `n` and `m` are updated for each iteration based on the input, and the loop completes after `t` iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, where 1 ≤ t ≤ 100. For each test case, it reads a pair of integers `n` and `m` from the input, where 1 ≤ n, m ≤ 100. It then checks if `n` is greater than or equal to `m` and if the difference `(n - m)` is even. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. After processing all `t` test cases, the function completes and the program returns to its caller.

