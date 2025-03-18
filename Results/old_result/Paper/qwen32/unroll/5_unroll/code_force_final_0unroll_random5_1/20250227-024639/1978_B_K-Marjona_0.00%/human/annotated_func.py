#State of the program right berfore the function call: Each test case consists of three integers n, a, and b (1 ≤ n, a, b ≤ 10^9), where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The output state consists of t lines, each representing the total cost of selling n buns given the usual price a and the modified price b for the first k buns, where k is the minimum of n and the difference between b and a. If b is less than or equal to a, the total cost is simply n multiplied by a. Otherwise, the total cost is calculated as the sum of the arithmetic series for the first k buns at the modified price plus the cost of the remaining (n-k) buns at the usual price.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: `n` (the number of buns), `a` (the usual price of a bun), and `b` (the price of the first bun to be sold at a modified price). For each test case, it calculates and returns the total cost of buying `n` buns, where the first bun is sold at the modified price `b`, and the remaining `n-1` buns are sold at the usual price `a`. If the modified price `b` is less than or equal to the usual price `a`, all buns are sold at the usual price `a`.

