def func_1(cost_price, selling_price):
    return cost_price == selling_price
assert func_1(1500, 1200) == False
assert func_1(100, 100) == True
assert func_1(2000, 5000) == False