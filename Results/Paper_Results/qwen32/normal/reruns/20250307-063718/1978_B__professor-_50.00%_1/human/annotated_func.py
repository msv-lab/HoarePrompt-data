#State of the program right berfore the function call: Each test case consists of three integers n, a, and b (1 ≤ n, a, b ≤ 10^9) where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price. There are t (1 ≤ t ≤ 10^4) such test cases.
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
        
    #State: All test cases have been processed and their respective outputs have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: `n` (the number of buns), `a` (the usual price of a bun), and `b` (the price of the first bun to be sold at a modified price). For each test case, it calculates and prints the total cost of selling all `n` buns, considering that the first bun is sold at the modified price `b`, and the remaining `n-1` buns are sold at the usual price `a`.

