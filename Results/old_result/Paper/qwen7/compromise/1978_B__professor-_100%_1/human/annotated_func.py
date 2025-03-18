#State of the program right berfore the function call: t is a positive integer indicating the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State: Output State: The output state will consist of `t` lines, where each line contains the result of the calculation based on the values of `n`, `a`, and `b` for each test case. If `b <= a`, it prints `n * a`. If `b - a >= n`, it prints `int((2 * b - n + 1) * n // 2)`. Otherwise, it prints `int((b - a) * (b - a + 1) // 2 + a * n)`.
#Overall this is what the function does:The function processes a series of test cases, each containing three positive integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun (b). For each test case, it calculates the total cost of buying n buns under specific pricing conditions. If the price of the first bun (b) is less than or equal to the usual price (a), it calculates the total cost as n times a. If the difference between b and a is greater than or equal to n, it calculates the total cost using the formula `(2 * b - n + 1) * n // 2`. Otherwise, it uses the formula `(b - a) * (b - a + 1) // 2 + a * n` to calculate the total cost. The function outputs the calculated total cost for each test case.

