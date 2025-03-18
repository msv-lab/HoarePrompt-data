#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n and m are integers such that 1 <= n, m <= 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: t test cases have been processed, and for each test case, 'YES' is printed if n is greater than or equal to m and the difference (n - m) is even; otherwise, 'NO' is printed. The values of t, n, and m are unchanged from their initial state, except they have been used to determine the output for each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `m`. For each test case, it prints 'YES' if `n` is greater than or equal to `m` and the difference (`n - m`) is even; otherwise, it prints 'NO'. The function does not modify the input values but uses them to determine the output for each test case.

