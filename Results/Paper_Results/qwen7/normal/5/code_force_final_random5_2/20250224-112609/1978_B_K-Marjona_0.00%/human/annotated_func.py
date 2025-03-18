#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price (0 ≤ k ≤ min(n, b)).
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: t is a positive integer representing the number of test cases. For each test case, n is the number of buns, a is the usual price of a bun, b is the price of the first bun to be sold at a modified price, and k is the minimum value between n and b - a. After all iterations of the loop, if b > a, then k remains unchanged from its initial value. If b ≤ a, then k remains unchanged from its initial value as well. The final output will be calculated based on the values of n, a, b, and k for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun to be sold at a modified price (b). It calculates the total cost of buying n buns under the given pricing conditions and prints the result for each test case. If the modified price (b) is less than or equal to the usual price (a), it calculates the total cost based on the usual price. Otherwise, it calculates the total cost considering both the usual and modified prices for the respective buns.

