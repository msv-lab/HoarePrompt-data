#State of the program right berfore the function call: n, m, r are positive integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are positive integers such that 1 <= s_i, b_i <= 1000.**
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
    #State of the program after the if-else block has been executed: *n, m, r are positive integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are positive integers such that 1 <= s_i, b_i <= 1000. s and b are lists of integers created by mapping the input split by space to integers. min_buy_price is the minimum value in list s. max_sell_price is the maximum value in list b. If max_sell_price <= min_buy_price, r is printed. Otherwise, total_bourles is the product of max_shares and max_sell_price added to remaining_bourles.
#Overall this is what the function does:The function `func` reads input values for positive integers n, m, r, as well as lists of integers s and b. It calculates the minimum buy price from list s and the maximum sell price from list b. If the maximum sell price is less than or equal to the minimum buy price, it prints the initial value of r. Otherwise, it calculates the total bourles by determining the maximum number of shares that can be bought at the minimum price, the remaining bourles after purchasing those shares, and then adding the profit from selling those shares at the maximum price. The function does not explicitly return a value.

