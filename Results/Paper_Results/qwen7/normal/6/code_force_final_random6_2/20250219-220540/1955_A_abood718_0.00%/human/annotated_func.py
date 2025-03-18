#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, a, and b such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30, where n is the number of yogurts Maxim wants to buy, a is the price for one yogurt, and b is the price for two yogurts on promotion.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X)
            print(X * C + B)
        
    #State: Output State: The loop has executed for all iterations, meaning `i` is now equal to the total number of test cases entered. For each test case, the value of `A` is the last input integer provided, `B` is the second input integer, and `C` is the third input integer. Depending on the conditions met within the loop:
    #
    #- If `B * 2 < C`, the output for that test case was `A * B`.
    #- If `B * 2 >= C` and `A` is even, the output for that test case was `int(A * C / 2)`.
    #- If `B * 2 >= C` and `A` is odd, the output for that test case was `X * C + B`, where `X = A // 2`.
    #
    #The final state of the loop will reflect these outputs for each test case, with `i` being the total number of iterations completed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of yogurts Maxim wants to buy (n), the price for one yogurt (a), and the price for two yogurts on promotion (b). For each test case, it calculates the minimum cost for Maxim to buy n yogurts based on the given prices and promotional offer. If the promotional price for two yogurts is cheaper than the individual price, it uses the promotional price to calculate the cost. Otherwise, it checks if the number of yogurts is even or odd to determine the optimal way to minimize the cost. The function does not return any value but prints the total cost for each test case.

