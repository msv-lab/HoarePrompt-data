#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: The loop has finished executing all t iterations, and for each iteration, the output is determined based on the conditions provided in the loop body. The values of t, n, a, and b are not retained after each iteration, and the loop does not modify any variables outside its scope.
#Overall this is what the function does:The function `func` reads an integer `t` (where `1 ≤ t ≤ 10^4`) representing the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` (where `1 ≤ n, a, b ≤ 10^9`). Depending on the values of `a` and `b`, it calculates and prints a result for each test case. The function does not retain any values between test cases and does not modify any external variables. After processing all `t` test cases, the function completes, and the program state is such that all test cases have been processed and their respective results have been printed.

