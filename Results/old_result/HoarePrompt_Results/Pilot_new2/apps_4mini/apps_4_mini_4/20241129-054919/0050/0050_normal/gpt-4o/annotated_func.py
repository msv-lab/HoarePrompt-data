#State of the program right berfore the function call: n is a positive integer (1 <= n <= 30), m is a positive integer (1 <= m <= 30), r is a positive integer (1 <= r <= 1000); s is a list of n integers where each integer si represents the price of shares (1 <= si <= 1000), and b is a list of m integers where each integer bi represents the selling price of shares (1 <= bi <= 1000).
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `r` are positive integers within the specified ranges. If `max_sell_price` is less than or equal to `min_buy_price`, no shares can be bought or sold. Otherwise, `max_shares` is calculated as `r // min_buy_price`, `remaining_bourles` is the remainder of `r` when divided by `min_buy_price`, and `total_bourles` is computed as `max_shares * max_sell_price + remaining_bourles`, with `total_bourles` being printed.
#Overall this is what the function does:The function accepts two lists of integers representing share prices and selling prices, along with three positive integers `n`, `m`, and `r`. It determines whether purchases can be made based on the prices, and if so, calculates and prints the total amount of money obtained from selling the shares. If no shares can be bought or sold, it prints the value of `r`.

