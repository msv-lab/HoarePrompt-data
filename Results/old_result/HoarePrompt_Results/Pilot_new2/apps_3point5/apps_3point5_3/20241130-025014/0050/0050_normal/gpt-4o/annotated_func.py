#State of the program right berfore the function call: 
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
    #State of the program after the if-else block has been executed: *`n`, `m`, and `r` are integers obtained by splitting the input by spaces. `b` is a list of integers. `min_buy_price` is the minimum value in the list `b`, and `max_sell_price` is the maximum value in the list `b`. If `max_sell_price <= min_buy_price`, then `r` is printed. Otherwise, `total_bourles` is printed, and no other variables are affected.
#Overall this is what the function does:The function reads input for integers `n`, `m`, and `r`, as well as lists of integers `s` and `b`. It calculates `min_buy_price` as the minimum value in list `s` and `max_sell_price` as the maximum value in list `b`. If `max_sell_price` is less than or equal to `min_buy_price`, it prints the value of `r`. Otherwise, it computes `max_shares`, `remaining_bourles`, and `total_bourles` based on the given conditions and prints `total_bourles`. The function does not accept any parameters and does not return anything.

