#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: `t` is an integer such that 1 <= t <= 1000, and for each test case, `k`, `x`, and `a` are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9. The file opened by `open(0)` must have at least `t + 1` lines. For each line `s` from the second to the `t + 1`-th line, `k`, `x`, and `a` are the integers read from that line. If `x < k - 1`, then the output is 'YES' if `a` is greater than or equal to `x + 1`, otherwise 'NO'. If `x == k - 1`, then the output is 'YES' if `a` is greater than or equal to `x + 2`, otherwise 'NO'. If `x > k - 1`, then `z` is updated by the nested loop to `z + (x - k + 3) * (z // (k - 1) + 1)`, and the output is 'YES' if `a` is greater than or equal to `z`, otherwise 'NO'.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input, where each test case is defined by three integers `k`, `x`, and `a` (with constraints 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9). For each test case, it determines whether a certain condition is met and prints 'YES' or 'NO' accordingly. Specifically, if `x < k - 1`, it prints 'YES' if `a` is greater than or equal to `x + 1`, otherwise 'NO'. If `x == k - 1`, it prints 'YES' if `a` is greater than or equal to `x + 2`, otherwise 'NO'. If `x > k - 1`, it calculates a value `z` using a nested loop and prints 'YES' if `a` is greater than or equal to `z`, otherwise 'NO'. After processing all test cases, the function does not return any value.

