#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State: Output State: The output state will consist of a series of integers printed for each test case. For each test case, if \( b \leq a \), it will print \( n \times a \). If \( b - a \geq n \), it will print \( \frac{(2 \times b - n + 1) \times n}{2} \). Otherwise, it will print \( \frac{(b - a) \times (b - a + 1)}{2} + a \times n \).
    #
    #This output state represents the result of processing each test case according to the given conditions and calculations within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun (b). For each test case, it calculates the total cost of the buns based on specific conditions and prints the result. If the first bun is cheaper than or equal to the usual price, it prints the total cost as if all buns were sold at the usual price. If the difference between the first bun's price and the usual price is greater than or equal to the number of buns, it calculates the total cost using a specific formula. Otherwise, it uses another formula to calculate the total cost.

