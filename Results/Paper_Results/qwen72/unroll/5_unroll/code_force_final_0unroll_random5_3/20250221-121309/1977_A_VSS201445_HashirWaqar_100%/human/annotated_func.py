#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, and for each test case, n and m are integers where 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: t is an integer where 1 <= t <= 100, and for each test case, n and m are integers where 1 <= n, m <= 100. The loop has finished executing, and the output for each test case is either 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from the input, where `1 <= t <= 100`, indicating the number of test cases. For each test case, it reads two integers `n` and `m` (where `1 <= n, m <= 100`) from the input. The function then checks if `n` is greater than or equal to `m` and if the difference `(n - m)` is even. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes, and the output for each test case is either 'YES' or 'NO' based on the conditions. The final state of the program is that all test cases have been processed and the corresponding outputs have been printed.

