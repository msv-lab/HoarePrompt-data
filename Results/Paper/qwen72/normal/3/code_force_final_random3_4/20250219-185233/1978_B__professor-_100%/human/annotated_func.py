#State of the program right berfore the function call: The function should take three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: `t` is 0, `n`, `a`, and `b` are updated to the values provided by the user for each iteration. The values of `n`, `a`, and `b` at the end of the loop are the values provided in the last iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the user, where 1 ≤ n, a, b ≤ 10^9. Depending on the relationship between `a` and `b`, it calculates and prints a specific integer result for each test case. After processing all test cases, the function completes, and the final state is that `t` is 0, and `n`, `a`, and `b` hold the values from the last test case.

