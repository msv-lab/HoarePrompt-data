(n, m, r) = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))
min_buy_price = min(s)
max_sell_price = max(b)
if max_sell_price <= min_buy_price:
    print(r)
else:
    max_shares = r // min_buy_price
    remaining_bourles = r % min_buy_price
    total_bourles = max_shares * max_sell_price + remaining_bourles
    print(total_bourles)