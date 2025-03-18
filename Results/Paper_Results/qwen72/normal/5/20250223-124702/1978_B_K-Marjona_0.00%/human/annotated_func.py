#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop executes t times, and for each iteration, it reads n, a, and b from input, calculates k as the minimum of n and (b - a), and prints the result of the calculation based on the conditions provided. The values of t, n, a, and b are not retained between iterations, and the loop does not modify any variables outside of its scope.
#Overall this is what the function does:The function `func` reads an integer `t` from input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from input. It then calculates a value based on these inputs and prints the result. The calculation is as follows: if `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it prints a more complex expression involving `n`, `a`, and `b`. The function does not return any values; it only prints the results to the console. After the function concludes, the values of `t`, `n`, `a`, and `b` are not retained, and the function does not modify any external variables.

