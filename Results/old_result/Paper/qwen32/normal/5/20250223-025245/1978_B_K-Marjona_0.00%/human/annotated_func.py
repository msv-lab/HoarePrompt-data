#State of the program right berfore the function call: Each test case consists of three integers n, a, and b (1 ≤ n, a, b ≤ 10^9) where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: `n`, `a`, `b`, and `k` are the values from the last test case, where `k` is `min(n, b - a)` for that test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: `n` (the number of buns), `a` (the usual price of a bun), and `b` (the price of the first bun to be sold at a modified price). For each test case, it calculates and prints the total cost of purchasing all `n` buns, considering that the first `k` buns are sold at a decreasing price starting from `b` down to `b-k+1` (where `k` is the minimum of `n` and `b-a`), and the remaining buns are sold at the usual price `a`. If `b` is less than or equal to `a`, all buns are sold at the usual price `a`.

