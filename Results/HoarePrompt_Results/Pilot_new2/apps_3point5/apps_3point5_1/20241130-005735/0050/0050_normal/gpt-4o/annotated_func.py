#State of the program right berfore the function call: **Precondition**: **n, m, and r are integers such that 1 <= n <= 30, 1 <= m <= 30, and 1 <= r <= 1000. s_i and b_i are integers indicating the prices of buying and selling shares, respectively, such that 1 <= s_i, b_i <= 1000.**
def func():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_buy_price = min(s)
    max_sell_price = max(b)
    if (max_sell_price <= min_buy_price) :
        print(r)
    else :
        max_shares = r // min_buy_price
        remaining_bourles = r % min_buy_price
        total_bourles = max_shares * max_sell_price + remaining_bourles
        print(total_bourles)
    #State of the program after the if-else block has been executed: *n, m, r are integers such that 1 <= n <= 30, 1 <= m <= 30, and 1 <= r <= 1000. s_i and b_i are integers indicating the prices of buying and selling shares, respectively, such that 1 <= s_i, b_i <= 1000. n, m, and r are assigned values based on the input split using map and int functions. s is a list of integers created from the input split and mapped to integers. b is a list of integers created from the input split and mapped to integers. min_buy_price is the minimum value in the list `s`. max_sell_price is the maximum value in the list `b`. If max_sell_price <= min_buy_price, then r. Otherwise, `total_bourles` is printed which is the calculated value of `max_shares` multiplied by `max_sell_price` plus `remaining_bourles`. All other variables retain their values from before the code execution.
#Overall this is what the function does:The function `func` reads input values for the number of shares, buying prices, and selling prices. It then calculates the minimum buying price and the maximum selling price. If the maximum selling price is less than or equal to the minimum buying price, it prints the initial investment `r`. Otherwise, it calculates the maximum number of shares that can be bought with the initial investment, the remaining amount of money after buying those shares, and then calculates the total profit that can be obtained by selling the maximum number of shares at the maximum selling price. The function does not accept any parameters and returns the total profit obtained from buying and selling shares based on the input prices.

