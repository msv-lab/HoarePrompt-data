#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State: `t` is 0, `n` is an input integer, `a` is an input integer, `b` is an input integer.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun to be sold at a modified price (b). For each test case, it calculates and prints the total revenue generated from selling all buns based on the given conditions. If the modified price (b) is less than or equal to the usual price (a), it prints the total revenue as if all buns were sold at the usual price. If the difference between the modified price and the usual price is greater than or equal to the number of buns, it calculates the revenue using a specific formula. Otherwise, it uses another formula to calculate the revenue.

