#State of the program right berfore the function call: The function should accept two parameters, n and m, where n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The function should also handle multiple test cases, where the number of test cases t is a positive integer such that 1 <= t <= 10^4.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: After the loop executes all the iterations, the variable `t` will be unchanged, and for each iteration, the variables `n` and `m` will be updated based on the input provided for that iteration. The variable `ans` will be calculated and printed for each iteration, and its value will be `n` plus the sum of `(n + b) // (b * b)` for all `b` from 2 to `min(n, m)`. The final state of `n` and `m` will be the values provided in the last test case, and `ans` will be the last calculated value before the loop ends.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `m` from the input, where `1 <= n, m <= 2 * 10^6`. The function calculates a value `ans` for each test case, which is the sum of `n` and the expression `(n + b) // (b * b)` for all integers `b` from 2 to `min(n, m)`. The calculated value `ans` is printed for each test case. After processing all test cases, the function terminates without returning any value. The final state of the program includes the values of `n` and `m` from the last test case, and the last calculated value of `ans` is printed.

