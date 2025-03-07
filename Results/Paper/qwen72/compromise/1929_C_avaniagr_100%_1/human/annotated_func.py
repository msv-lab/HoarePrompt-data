#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, k, x, and a are integers for each test case where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, and for each test case, `k`, `x`, and `a` are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9. The loop has executed `t` times, and for each execution, the values of `k`, `x`, and `a` are taken from the corresponding line in the input. If `x < k - 1`, the loop checks if `a` is greater than or equal to `x + 1` and prints 'YES' if true, otherwise prints 'NO'. If `x == k - 1`, the loop checks if `a` is greater than or equal to `x + 2` and prints 'YES' if true, otherwise prints 'NO'. If `x > k - 1`, the loop calculates `z` starting from `k - 2` and updates it by adding `z // (k - 1) + 1` for `x - k + 3` iterations. If `a` is greater than or equal to the final value of `z`, it prints 'YES', otherwise it prints 'NO'.
#Overall this is what the function does:The function reads input from standard input, where the first line specifies the number of test cases `t` (1 <= t <= 1000). For each test case, it reads three integers `k`, `x`, and `a` (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9). It then determines whether a certain condition involving `k`, `x`, and `a` is met and prints 'YES' or 'NO' accordingly. Specifically, if `x < k - 1`, it checks if `a >= x + 1`. If `x == k - 1`, it checks if `a >= x + 2`. If `x > k - 1`, it calculates a value `z` starting from `k - 2` and updates it by adding `z // (k - 1) + 1` for `x - k + 3` iterations, then checks if `a >= z`. After processing all test cases, the function has printed 'YES' or 'NO' for each case based on these conditions.

