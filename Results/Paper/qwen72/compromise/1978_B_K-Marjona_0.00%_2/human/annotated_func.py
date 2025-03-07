#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `a`, and `b` from the input, computes a value based on the given conditions, and prints the result. The values of `t`, `n`, `a`, and `b` are not retained between iterations, and the loop does not modify any variables outside of its scope. Therefore, the state of `t` remains unchanged, and the state of `n`, `a`, and `b` is reset for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` (1 ≤ n, a, b ≤ 10^9) from the input. It then computes a value based on the following conditions: if `b` is less than or equal to `a`, it prints `a * n`; otherwise, it calculates and prints a more complex expression involving `n`, `a`, and `b`. The function does not return any value; it only prints the results for each test case. After the function concludes, the state of `t` remains unchanged, and the values of `n`, `a`, and `b` are not retained between iterations.

