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
        
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the `t` test cases, `k`, `x`, and `a` are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9. For each test case, if `x < k - 1`, then the condition `a >= x + 1` or `a < x + 1` holds. If `x == k - 1`, then the condition `a >= x + 2` or `a < x + 2` holds. If `x >= k - 2` and `x != k - 1`, then `z` is the result of the loop body being applied `x - k + 3` times, and the condition `a >= z` or `a < z` holds.
#Overall this is what the function does:The function reads input from standard input, where each line after the first contains three integers `k`, `x`, and `a`. For each test case, it checks if `a` meets certain conditions based on the values of `k` and `x`. If `x < k - 1`, it prints 'YES' if `a >= x + 1` and 'NO' otherwise. If `x == k - 1`, it prints 'YES' if `a >= x + 2` and 'NO' otherwise. If `x > k - 1`, it calculates a value `z` using a loop and prints 'YES' if `a >= z` and 'NO' otherwise. The function does not return any value.

