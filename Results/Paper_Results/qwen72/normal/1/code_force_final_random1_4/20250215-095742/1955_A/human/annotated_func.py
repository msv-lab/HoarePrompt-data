#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n, a, and b are integers such that 1 <= n <= 100, 1 <= a, b <= 30, where n is the number of yogurts Maxim wants to buy, a is the price for one yogurt, and b is the price for two yogurts on promotion.
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
        
    #State: After all iterations, `t` remains an integer such that 1 <= t <= 10^4, `i` is `t - 1`, and the values of `A`, `B`, and `C` for each test case are processed according to the conditions in the loop. For each test case, if `B * 2 < C`, the output is `A * B`. If `A` is even, the output is `int(A * C / 2)`. If `A` is odd, the output is `X * C + B` where `X = A // 2`. The values of `A`, `B`, and `C` for each test case are reset for the next iteration, and the loop processes `t` test cases in total.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `A`, `B`, and `C`, representing the number of items, the price per item, and the promotional price for two items, respectively. The function calculates and prints the minimum cost to purchase `A` items based on the following rules: if the cost of two items individually (`B * 2`) is less than the promotional price (`C`), it prints `A * B`. If `A` is even, it prints `int(A * C / 2)`. If `A` is odd, it prints `X * C + B` where `X = A // 2`. After processing all test cases, the function has printed the minimum cost for each test case.

