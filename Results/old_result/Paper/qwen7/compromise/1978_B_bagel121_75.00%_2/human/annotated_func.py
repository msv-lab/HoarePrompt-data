#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
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
        
    #State: Output State: The total cost calculated for each test case based on the given conditions, printed for each iteration of the loop. If the usual price of a bun (a) is greater than or equal to the modified price of the first bun (b), the total cost is simply the usual price multiplied by the number of buns (n). Otherwise, the total cost is calculated using the formula involving the modified price, the difference between the usual and modified prices, and the number of buns.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers \( n \), \( a \), and \( b \), representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. For each test case, it calculates the total cost of selling \( n \) buns, considering the modified price for the first bun and the usual price for the rest. If the usual price \( a \) is greater than or equal to the modified price \( b \), the total cost is simply \( n \times a \). Otherwise, it uses a specific formula to compute the total cost, taking into account the modified price, the difference between the usual and modified prices, and the number of buns. The function prints the total cost for each test case.

