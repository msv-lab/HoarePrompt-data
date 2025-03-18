#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 30 and 1 <= m <= 30; r is an integer such that 1 <= r <= 1000; s is a list of n integers where each element s[i] satisfies 1 <= s[i] <= 1000; b is a list of m integers where each element b[j] satisfies 1 <= b[j] <= 1000.
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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 <= `n` <= 30; `m` is an integer such that 1 <= `m` <= 30; `r` is an input integer; `s` is a list of `n` integers derived from input; `b` is a list of `m` integers derived from input where each element `b[j]` satisfies 1 <= `b[j]` <= 1000; `min_buy_price` is the minimum value from list `s`; `max_sell_price` is the maximum value from list `b`. If `max_sell_price` is less than or equal to `min_buy_price`, the value of `r` has been printed. Otherwise, `max_sell_price` is greater than `min_buy_price`; `max_shares` is equal to `r // min_buy_price`; `remaining_bourles` is equal to `r % min_buy_price`; and `total_bourles` is equal to `max_shares * max_sell_price + remaining_bourles`, which has been printed.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `r`, and two lists `s` and `b`. It calculates the minimum buy price from list `s` and the maximum sell price from list `b`. If the maximum sell price is less than or equal to the minimum buy price, it prints the value of `r`. Otherwise, it calculates the maximum number of shares that can be bought with `r` at the minimum buy price, computes the remaining money after the purchase, and then calculates the total amount of money that would be received from selling those shares at the maximum sell price, plus any remaining money from the initial amount. Finally, it prints this total amount. The function does not return any values, it only prints the results.

