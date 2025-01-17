#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State of the program after the  for loop has been executed: `t` must be a positive integer, and the program will process each test case based on the conditions provided within the loop. For each test case, if `b <= a`, the output is `n * a`. Otherwise, if `b - a >= n`, the output is `int((2 * b - n + 1) * n / 2)`. If `b - a < n`, the output is `int((b - a) / 2 * (b - a + 1) + a * n)`. After processing all test cases, no specific values for `n`, `a`, and `b` will be retained, as they are redefined for each iteration. The final state of the program will be that all test cases have been processed according to the given conditions.
#Overall this is what the function does:The function accepts a parameter `t`, a positive integer representing the number of test cases. For each test case, it processes three positive integers `n`, `a`, and `b` (where \(1 \leq n, a, b \leq 10^9\)). Based on the value of `b` relative to `a`, the function calculates and prints one of three possible outputs:

1. If `b <= a`, the output is `n * a`.
2. If `b - a >= n`, the output is `int((2 * b - n + 1) * n / 2)`.
3. If `b - a < n`, the output is `int((b - a) / 2 * (b - a + 1) + a * n)`.

After processing all test cases, the function does not retain any specific values for `n`, `a`, and `b`, as these are redefined for each iteration. The final state of the program will be that all test cases have been processed according to the given conditions.

