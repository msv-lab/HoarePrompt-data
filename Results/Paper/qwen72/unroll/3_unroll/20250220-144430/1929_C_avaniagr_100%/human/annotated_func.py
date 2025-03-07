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
        
    #State: The values of `t`, `k`, `x`, and `a` remain unchanged, but the loop will have printed 'YES' or 'NO' for each test case based on the conditions provided in the loop body.
#Overall this is what the function does:The function `func` reads input from standard input, processes multiple test cases, and prints 'YES' or 'NO' for each test case based on specific conditions. Each test case consists of three integers: `k`, `x`, and `a`. The function does not return any value, but it modifies the program state by printing the results. The values of `t`, `k`, `x`, and `a` remain unchanged after the function concludes.

