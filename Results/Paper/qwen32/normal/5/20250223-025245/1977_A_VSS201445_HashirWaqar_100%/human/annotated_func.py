#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has executed `t` times, where `t` is the initial integer input such that 1 <= t <= 100. For each of the `t` iterations, two integers `n` and `m` were provided, and the program printed 'YES' if `n` is greater than or equal to `m` and the difference (`n - m`) is even, otherwise it printed 'NO'. The values of `t`, `n`, and `m` remain unchanged after the loop finishes executing all iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the next `t` lines, it reads two integers `n` and `m`. It then prints 'YES' if `n` is greater than or equal to `m` and the difference (`n - m`) is even; otherwise, it prints 'NO'.

