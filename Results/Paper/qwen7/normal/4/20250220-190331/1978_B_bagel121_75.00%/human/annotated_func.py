#State of the program right berfore the function call: t is a positive integer indicating the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: `t` is 0, `n` is an input integer, `a` is an input integer, `b` is an input integer, `k` is the minimum value between `b - a + 1` and `n`, `ans` is calculated as `int((b + (b - k + 1)) / 2 * k)`, `p2` is `(n - k) * a` for the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun to be sold at a modified price (b). For each test case, it calculates and prints the total cost based on the given conditions. If the usual price of a bun is greater than or equal to the modified price, it simply prints the total cost as `n * a`. Otherwise, it calculates the total cost considering the modified price for the first few buns and the usual price for the remaining buns.

