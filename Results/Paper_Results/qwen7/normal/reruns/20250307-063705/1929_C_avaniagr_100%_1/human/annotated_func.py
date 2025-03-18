#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
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
        
    #State: Output State: After the loop executes all its iterations, the variable `t` remains a positive integer such that \(1 \leq t \leq 1000\). The variables `k`, `x`, and `a` retain their final values after the last iteration of the loop. The variable `z` is calculated based on the conditions provided within the loop:
    #
    #- If `x < k - 1` and `a >= x + 1`, `z` is increased by `z // (k - 1) + 1` for each iteration from 0 to `x - k + 2`.
    #- If `x == k - 1` and `a >= x + 2`, `z` is increased by `z // (k - 1) + 1` for each iteration from 0 to `x - k + 2`.
    #- If `x >= k - 1`, `z` is increased by `z // (k - 1) + 1` for each iteration from 0 to `x - k + 2`.
    #
    #If `a` is greater than or equal to `z` after all iterations, `z` is updated to `3 * (z + z // (k - 1) + 1)`. Otherwise, `z` retains its value after the last iteration.
    #
    #In summary, the final state of `z` will depend on the specific values of `k`, `x`, and `a` after all iterations, with `z` being updated according to the rules defined within the loop.
#Overall this is what the function does:The function reads input values for `t`, `k`, `x`, and `a` from standard input. It then iterates through these values, performing calculations based on the given conditions. Specifically, it calculates a value `z` based on the relationship between `x` and `k`, and checks if `a` is greater than or equal to `z`. If so, it prints 'YES', otherwise it prints 'NO'. The function does not return any value but prints 'YES' or 'NO' for each set of input values.

