#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4). Each of the following t test cases consists of three integers n, a, and b (1 ≤ n, a, b ≤ 10^9), where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: t is 0; all test cases have been processed.
#Overall this is what the function does:The function calculates and prints the minimum total cost to buy all buns for each of the given test cases, considering a special price for the first bun in each case.

