#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function should handle multiple test cases, indicated by an integer `t` where 1 <= t <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has executed all iterations, and for each test case, it has printed 'YES' if `n` is greater than or equal to `m` and the difference `(n - m)` is even, otherwise it has printed 'NO'. The variables `n` and `m` are no longer in scope after the loop completes, and the variable `t` (number of test cases) is unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two non-negative integers `n` and `m` from the input. It then prints 'YES' if `n` is greater than or equal to `m` and the difference `(n - m)` is even; otherwise, it prints 'NO'. After processing all test cases, the function completes, and the variables `n` and `m` are no longer in scope, while `t` remains unchanged. The function does not return any value.

