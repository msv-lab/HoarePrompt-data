#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 30; r is a positive integer such that 1 <= r <= 1000; s is a list of n positive integers where each integer s_i (1 <= s_i <= 1000) represents the price to buy shares; b is a list of m positive integers where each integer b_i (1 <= b_i <= 1000) represents the price to sell shares.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `r` are positive integers (1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000). If the maximum sell price is less than or equal to the minimum buy price, the function returns the value of `r`. Otherwise, the function calculates `max_shares` as `r // min_buy_price`, `remaining_bourles` as `r % min_buy_price`, and prints the total amount of bourles calculated as `max_shares * max_sell_price + remaining_bourles`.
#Overall this is what the function does:The function reads three positive integers `n`, `m`, and `r`, which represent the number of buying prices, selling prices, and available bourles respectively. It then reads two lists: `s`, containing `n` buying prices, and `b`, containing `m` selling prices. If the maximum selling price is less than or equal to the minimum buying price, it prints the available bourles `r`. Otherwise, it calculates the maximum number of shares that can be bought with `r` using the minimum buying price, determines the remaining bourles after buying those shares, and computes the total bourles that would be obtained by selling the shares at the maximum selling price plus the remaining bourles. The function does not accept parameters directly but interacts with user input instead.

