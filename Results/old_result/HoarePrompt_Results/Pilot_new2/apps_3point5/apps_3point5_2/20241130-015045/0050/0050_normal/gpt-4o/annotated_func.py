#State of the program right berfore the function call: n, m, r are positive integers such that 1 <= n, m <= 30 and 1 <= r <= 1000. s_i and b_i are positive integers representing the price of shares, such that 1 <= s_i, b_i <= 1000.**
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
    #State of the program after the if-else block has been executed: *n, m, r are positive integers such that 1 <= n, m <= 30 and 1 <= r <= 1000. s_i and b_i are positive integers representing the price of shares, such that 1 <= s_i, b_i <= 1000. n, m, r are assigned the integer values obtained from splitting the input. s is a list of integers obtained by splitting the input. b is a list containing integers obtained from splitting the input. min_buy_price is the minimum price among the prices in list s. max_sell_price is the maximum price among the prices in list b. If max_sell_price <= min_buy_price, then max_shares is equal to the result of integer division r by min_buy_price. remaining_bourles = r % min_buy_price. total_bourles = max_shares * max_sell_price + remaining_bourles. Otherwise, n, m, r, s, b, min_buy_price, max_sell_price, max_shares, remaining_bourles, total_bourles remain unchanged.
#Overall this is what the function does:The function `func` reads input values for the number of shares, prices of shares, and initial investment. It then calculates the maximum profit that can be obtained from buying and selling the shares based on the given parameters. If the maximum selling price is less than or equal to the minimum buying price, it prints the initial investment. Otherwise, it calculates the total profit by determining the maximum number of shares that can be bought with the initial investment, the remaining amount after buying shares, and the total profit from selling the bought shares. The function finally prints the total profit achieved.

