#State of the program right berfore the function call: The function should accept three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: The values of `n`, `a`, and `b` will be updated based on the input provided for each iteration of the loop. The variable `t` will be decremented by 1 for each iteration until it reaches 0. The loop will print a result for each iteration, but the values of `n`, `a`, and `b` will be reset to the next input values for the next iteration. Therefore, after all iterations, the values of `n`, `a`, and `b` will be the values provided in the last input, and `t` will be 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input, where 1 ≤ n, a, b ≤ 10^9. It then calculates and prints a result based on the values of `n`, `a`, and `b`. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates a value `ans` and a value `p2`, and prints their sum. After processing all test cases, the function completes, and the values of `n`, `a`, and `b` will be the values provided in the last test case, while `t` will be 0.

