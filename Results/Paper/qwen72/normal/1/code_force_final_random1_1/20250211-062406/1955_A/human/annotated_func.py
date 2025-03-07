#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n, a, and b are integers such that 1 <= n <= 100, 1 <= a, b <= 30, representing the number of yogurts to buy, the price per yogurt, and the promotional price for two yogurts, respectively.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: After the loop has executed all its iterations, `i` will be equal to `t - 1`, where `t` is the initial number of test cases. The values of `A`, `B`, and `C` will be the last set of inputs read from the user. If `B * 2 < C`, no changes are made to `A`, `B`, or `C`. If `B * 2 >= C` and `A` is even, no changes are made to `A`, `B`, or `C`. If `B * 2 >= C` and `A` is odd, `X` is set to `A // 2`.
#Overall this is what the function does:The function reads multiple sets of inputs from the user, each set containing three integers `A`, `B`, and `C`. For each set, it calculates and prints the minimum cost to buy `A` yogurts, considering both the regular price `B` and the promotional price `C` for two yogurts. If the promotional price for two yogurts is less than twice the regular price, it uses the promotional price to minimize the cost. If `A` is odd, it buys one additional yogurt at the regular price. The function does not return any value; it only prints the calculated costs for each test case. After processing all test cases, the function completes, and the final state includes the printed results for each test case.

