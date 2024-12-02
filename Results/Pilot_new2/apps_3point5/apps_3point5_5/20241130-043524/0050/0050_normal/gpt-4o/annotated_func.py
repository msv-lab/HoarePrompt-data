#State of the program right berfore the function call: **Precondition**: **n, m, r are integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are integers indicating the prices of shares such that 1 <= s_i, b_i <= 1000.**
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `r` are integers obtained from the input. `s` and `b` are lists of integers created by mapping the `int` function to the input. `min_buy_price` is the minimum value in list `s`, and `max_sell_price` is the maximum value in list `b`. If `max_sell_price` is less than or equal to `min_buy_price`, the program prints the value of `r`. Otherwise, `total_bourles` is calculated as the product of `max_shares` multiplied by `max_sell_price` added to `remaining_bourles`.
#Overall this is what the function does:The function `func` reads three integers `n`, `m`, and `r` from the input. It then reads two lists `s` and `b` of integers. The function calculates the minimum buy price from list `s` and the maximum sell price from list `b`. If the maximum sell price is less than or equal to the minimum buy price, it prints the value of `r`. Otherwise, it calculates the total bourles by considering the maximum number of shares that can be bought with `r`, the remaining bourles, and the maximum sell price. The function does not explicitly return any value.

