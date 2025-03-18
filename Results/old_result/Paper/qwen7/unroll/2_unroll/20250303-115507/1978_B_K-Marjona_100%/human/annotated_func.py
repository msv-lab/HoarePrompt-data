#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: Output State: The total cost calculated for each test case based on the given conditions. For each test case, if the price of the first bun (b) is greater than or equal to the usual price (a), the total cost is the sum of the first bun's discounted price multiplied by the minimum number of buns sold at the discounted price plus the usual price of the remaining buns. If the first bun's price is less than or equal to the usual price, the total cost is simply the usual price multiplied by the total number of buns.
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of buns (n), the usual price of a bun (a), and the price of the first bun to be sold at a modified price (b). For each test case, it calculates the total revenue generated from selling all buns based on the following rules: if the modified price (b) is greater than the usual price (a), it applies a discount to the first few buns and charges the usual price for the rest; otherwise, it charges the usual price for all buns. The function outputs the total revenue for each test case.

