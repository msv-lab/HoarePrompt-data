#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, a, and b such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30, where n is the number of yogurts Maxim wants to buy, a is the price for one yogurt, and b is the price for two yogurts on promotion.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: Output State: The output state will consist of a series of minimum costs for purchasing different numbers of yogurts based on the given conditions. For each test case, if buying more than one yogurt, the program calculates the cost of buying each yogurt individually (ans1) or buying them in pairs with a promotion (ans2), then prints the lower of the two costs. If buying just one yogurt, it simply prints the cost of one yogurt. The process repeats for each test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of yogurts `n`, the price for one yogurt `a`, and the price for two yogurts on promotion `b`. For each test case, it calculates the minimum cost for Maxim to buy `n` yogurts either by buying them individually or in pairs, depending on which option is cheaper. It then prints the minimum cost for each test case.

