#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: A series of 'YES' or 'NO' strings, one per test case, based on the conditions specified in the code.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `k`, `x`, and `a`. For each test case, it determines whether a certain condition involving these integers is met and prints 'YES' or 'NO' accordingly. The final state of the program is a series of 'YES' or 'NO' strings, one for each test case, indicating whether the condition is satisfied based on the input values.

