#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price, such that 1 \le n, a, b \le 10^9.
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
        
    #State of the program after the  for loop has been executed: `t` is an input integer greater than 0. For each iteration, `n` is an integer read from input, `a` is an integer read from input, and `b` is an integer read from input. After all iterations, the last printed value is determined based on the following conditions:
    #- If `b` is less than or equal to `a`, the last printed value is `n * a`.
    #- If `b` is greater than `a` and `b - a` is greater than or equal to `n`, the last printed value is `int((2 * b - n + 1) * n / 2).
    #- Otherwise, the last printed value is `int((b - a) / 2 * (b - a + 1) + a * n)`.
    #
    #The values of `n`, `a`, and `b` for each iteration do not affect the final printed value unless they are used in the conditions above. The final printed value is the result of the last condition met during the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( a \), and \( b \), where \( n \) represents the number of buns, \( a \) is the usual price of a bun, and \( b \) is the price of the first bun to be sold at a modified price. For each test case, the function calculates the total cost for \( n \) buns under the following conditions:
- If \( b \) is less than or equal to \( a \), the total cost is \( n \times a \).
- If \( b \) is greater than \( a \) and the difference between \( b \) and \( a \) is greater than or equal to \( n \), the total cost is calculated using the formula \( \text{int}((2 \times b - n + 1) \times n / 2) \).
- Otherwise, the total cost is calculated using the formula \( \text{int}((b - a) / 2 \times (b - a + 1) + a \times n) \).

The function reads \( t \) test cases from the input, processes each one according to the conditions described, and prints the total cost for each test case. The final state of the program after the function concludes is that it has processed all test cases and printed the total cost for each one, with the last printed value being the result of the last condition met during the loop iterations.

