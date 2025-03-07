#State of the program right berfore the function call: The function `func` is expected to be called with a list of test cases, where each test case is a tuple or list containing two integers n and m, such that 1 <= n, m <= 100. The function should handle up to 100 test cases.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has completed all iterations, `_` is equal to `int(input()) - 1`, and the final values of `n` and `m` are the integers provided by the user input for the last iteration. For each iteration, if `n` was greater than or equal to `m` and the difference `(n - m)` was an even number, 'YES' was printed; otherwise, 'NO' was printed. The initial condition `int(input())` must be greater than 0, and the loop has executed exactly `int(input())` times.
#Overall this is what the function does:The function `func` processes a series of test cases provided through user input. Each test case consists of two integers `n` and `m` (1 <= n, m <= 100). For each test case, the function prints 'YES' if `n` is greater than or equal to `m` and the difference `(n - m)` is even; otherwise, it prints 'NO'. The function handles up to 100 test cases, and the number of test cases is specified by the first user input. After processing all test cases, the function concludes without returning any value.

