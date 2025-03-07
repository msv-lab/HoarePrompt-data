#State of the program right berfore the function call: Each test case consists of three integers n, a, and b (1 ≤ n, a, b ≤ 10^9) where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price. There are t (1 ≤ t ≤ 10^4) such test cases.
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
        
    #State: The loop has processed all `t` test cases and printed the corresponding costs for each test case. The variables `n`, `a`, and `b` do not retain any specific values after the loop ends.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: `n` (number of buns), `a` (usual price of a bun), and `b` (modified price of the first bun). For each test case, it calculates and prints the total cost of purchasing all `n` buns, considering the first bun's price as `b` and the remaining buns' price as `a`.

