#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 30 and 1 <= m <= 30; r is an integer such that 1 <= r <= 1000; s is a list of n integers where each s[i] (1 <= s[i] <= 1000) represents the price to buy shares; b is a list of m integers where each b[j] (1 <= b[j] <= 1000) represents the price to sell shares.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `r` are integers between 1 and 30 and 1 and 1000 respectively; `s` is a list of `n` integers (1 <= s[i] <= 1000); `b` is a list of integers based on input; `min_buy_price` is the minimum value in the list `s`; and `max_sell_price` is the maximum value in list `b`. If `max_sell_price` is less than or equal to `min_buy_price`, the value of `r` is printed. Otherwise, `max_shares` is calculated as `r // min_buy_price`, `remaining_bourles` is `r % min_buy_price`, and `total_bourles` is computed as `max_shares * max_sell_price + remaining_bourles`, which is then printed.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `r`, and two lists `s` and `b` representing the prices to buy and sell shares, respectively. It calculates the minimum buy price from the list `s` and the maximum sell price from the list `b`. If the maximum sell price is less than or equal to the minimum buy price, it prints the initial integer `r`. Otherwise, it computes the maximum number of shares that can be bought with `r` at the minimum buy price, calculates the remaining funds after purchasing these shares, and then computes the total funds after selling the shares at the maximum sell price. The resulting total is printed.

