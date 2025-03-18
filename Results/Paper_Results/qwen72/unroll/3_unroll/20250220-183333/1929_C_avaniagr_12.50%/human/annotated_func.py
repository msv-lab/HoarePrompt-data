#State of the program right berfore the function call: The function `func` is expected to take input through standard input and process multiple test cases. Each test case contains three integers k, x, and a such that 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. The number of test cases t is an integer where 1 ≤ t ≤ 1000.
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
        
    #State: The output state after the loop executes all the iterations is that the function will have processed all `t` test cases, and for each test case, it will have printed 'YES' or 'NO' based on the conditions specified in the loop. The variables `k`, `x`, and `a` will be updated to their respective values for each test case, but their final values after the loop will be the values from the last test case. The variable `z` will be updated within the loop for each test case where `x` is greater than `k - 1`, but its final value will be the one computed for the last test case where `x` is greater than `k - 1`. The loop counter `_` will have completed all `t` iterations and will no longer be in use.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, each consisting of three integers `k`, `x`, and `a`. For each test case, it determines whether the value of `a` meets certain conditions based on `k` and `x`, and prints 'YES' if the condition is met, otherwise it prints 'NO'. The function processes all `t` test cases, where `t` is the number of test cases provided. After processing all test cases, the function has no return value, but the output consists of 'YES' or 'NO' for each test case. The final state of the program is that the input has been fully processed, and the results for each test case have been printed to the standard output.

