#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has executed `t` times, where `t` is the integer provided initially. For each of the `t` iterations, the program has read two integers `n` and `m`, and printed "YES" if `n` is greater than or equal to `m` and the difference `(n - m)` is even; otherwise, it printed "NO". The values of `n` and `m` are determined by the input provided for each iteration.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `m`. For each test case, it prints "YES" if `n` is greater than or equal to `m` and the difference `(n - m)` is even; otherwise, it prints "NO".

