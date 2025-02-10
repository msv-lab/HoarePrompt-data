#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, and for each of the t test cases, n and m are integers where 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: The loop has completed all iterations as specified by the initial input value `_`. For each iteration, the values of `n` and `m` were read from the input, and the conditions within the loop were evaluated. If `n` was less than `m`, "NO" was printed. If `n` was greater than or equal to `m` and both `n` and `m` were either both odd or both even, "YES" was printed. The loop has now finished executing, and no further iterations will occur.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 <= t <= 100. For each test case, it reads two integers `n` and `m` (1 <= n, m <= 100). It then evaluates the following conditions for each test case: if `n` is less than `m`, it prints "NO". If `n` is greater than or equal to `m` and both `n` and `m` are either both odd or both even, it prints "YES". After processing all test cases, the function completes its execution, and no further output is produced.

