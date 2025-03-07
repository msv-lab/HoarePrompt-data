#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: `t` is an input integer such that 0 <= t <= 1000, `k`, `x`, and `a` are input integers with the same constraints as the initial state, and the loop counter `_` is incremented by `t`. The conditions for `a` relative to `x`, `k`, and `z` are evaluated for each iteration, and the results are printed accordingly.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from user input. The function then evaluates whether `a` meets certain conditions relative to `k` and `x`. If `x` is less than `k - 1` and `a` is greater than or equal to `x + 1`, or if `x` equals `k - 1` and `a` is greater than or equal to `x + 3`, or if `x` is greater than `k - 1` and `a` is greater than or equal to a computed value `z`, it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value.

