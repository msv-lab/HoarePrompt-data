#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: The values of `t`, `k`, `x`, and `a` remain unchanged, but the loop has printed 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of three integers `k`, `x`, and `a`. For each test case, it determines and prints 'YES' if the value of `a` meets certain conditions based on `k` and `x`, and 'NO' otherwise. The conditions are as follows: if `x` is less than `k - 1`, `a` must be at least `x + 1`; if `x` equals `k - 1`, `a` must be at least `x + 2`; if `x` is greater than `k - 1`, `a` must be at least a calculated value `z`. The function does not return any value, but it prints the result for each test case. The values of `t`, `k`, `x`, and `a` remain unchanged after the function execution.

