#State of the program right berfore the function call: Each test case contains two integers n and m where 1 <= n, m <= 100. The function should handle multiple test cases, with the number of test cases t such that 1 <= t <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has finished executing all iterations, and for each test case, the output will be 'YES' if n is greater than or equal to m and the difference (n - m) is even, otherwise the output will be 'NO'. The values of n and m for each test case are processed and then discarded, so they do not persist after the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of two integers, `n` and `m`, where both are between 1 and 100 inclusive. The function reads the number of test cases `t` (1 <= t <= 100) and then, for each test case, it prints 'YES' if `n` is greater than or equal to `m` and the difference `(n - m)` is even; otherwise, it prints 'NO'. After processing all test cases, the function concludes, and the values of `n` and `m` for each test case are discarded.

