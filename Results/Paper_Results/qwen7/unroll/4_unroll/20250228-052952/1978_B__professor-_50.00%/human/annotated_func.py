#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State: Output State: The output state will consist of a series of integers printed as a result of the loop's execution. For each test case specified by the input integer `t`, the output will depend on the values of `n`, `a`, and `b` for that particular iteration. If `b <= a`, it will print `n * a`. If `b - a >= n`, it will print the value of \(\frac{(2 * b - n + 1) * n}{2}\). Otherwise, it will print the value of \(\frac{(b - a) * (b - a + 1)}{2} + a * n\).
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers (n, a, b). It calculates the total cost of buns based on the given prices and prints the total cost for each test case. Depending on the relationship between `a` and `b`, it uses different formulas to compute the total cost. If `b` is less than or equal to `a`, it simply prints `n * a`. If `b - a` is greater than or equal to `n`, it prints \(\frac{(2 * b - n + 1) * n}{2}\). Otherwise, it prints \(\frac{(b - a) * (b - a + 1)}{2} + a * n\). After processing all test cases, the function concludes with no return value, only printing the results.

