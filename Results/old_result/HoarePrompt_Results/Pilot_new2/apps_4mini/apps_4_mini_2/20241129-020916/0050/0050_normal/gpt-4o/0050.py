# Reading input
n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))

# Finding the minimum buy price and maximum sell price
min_buy_price = min(s)
max_sell_price = max(b)

# If the maximum sell price is less than or equal to the minimum buy price, no profit can be made
if max_sell_price <= min_buy_price:
    print(r)
else:
    # Calculate the maximum number of shares that can be bought with current bourles
    max_shares = r // min_buy_price
    # Calculate remaining bourles after buying shares
    remaining_bourles = r % min_buy_price
    # Calculate total bourles after selling all shares at maximum sell price
    total_bourles = max_shares * max_sell_price + remaining_bourles
    print(total_bourles)
