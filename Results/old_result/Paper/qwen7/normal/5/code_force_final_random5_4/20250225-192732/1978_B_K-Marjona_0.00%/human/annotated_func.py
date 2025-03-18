#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of three positive integers n, a, and b, where n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price (0 ≤ k ≤ min(n, b)).
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: Output State: The loop has executed for all the test cases provided by the user. For each test case, the variables `n`, `a`, and `b` represent the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively. The variable `k` is the minimum value between `n` and `b - a`. If `b` is greater than `a`, `k` is also the minimum value between `n` and `b - a`. The final output for each test case is calculated based on whether `b` is less than or equal to `a` or not, as described in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: the number of buns (n), the usual price of a bun (a), and the price of the first bun to be sold at a modified price (b). It calculates and prints the total cost based on these inputs. If the price of the first modified bun (b) is less than or equal to the usual price (a), it calculates the total cost as the usual price multiplied by the number of buns. Otherwise, it calculates the total cost considering both the usual and modified prices for the buns.

