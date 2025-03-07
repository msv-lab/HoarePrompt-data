#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: `t` is an input integer between 1 and 1000, `k` is an input integer where 2 <= `k` <= 30, `x` is an input integer where 1 <= `x` <= 100, and `a` is an input integer where 1 <= `a` <= 10^9. The loop has executed `t` times, and for each test case, the values of `k`, `x`, and `a` have been updated to the integers provided by the user input. If `x` < `k - 1`, the condition `a >= x + 1` has been checked and the appropriate output ('YES' or 'NO') has been printed. If `x` == `k - 1`, the condition `a >= x + 3` has been checked and the appropriate output ('YES' or 'NO') has been printed. If `x` > `k - 1`, `z` has been calculated as the sum of `z // (k - 1) + 1` for `i` from 0 to `x`, and the condition `a >= z` has been checked and the appropriate output ('YES' or 'NO') has been printed.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 <= t <= 1000) indicating the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9). The function evaluates a condition based on the values of `k`, `x`, and `a` and prints 'YES' if the condition is met, otherwise it prints 'NO'. Specifically, if `x` is less than `k - 1`, it checks if `a` is at least `x + 1`. If `x` equals `k - 1`, it checks if `a` is at least `x + 3`. If `x` is greater than `k - 1`, it calculates a value `z` as the sum of `z // (k - 1) + 1` for `i` from 0 to `x`, and checks if `a` is at least `z`. After processing all `t` test cases, the function concludes.

