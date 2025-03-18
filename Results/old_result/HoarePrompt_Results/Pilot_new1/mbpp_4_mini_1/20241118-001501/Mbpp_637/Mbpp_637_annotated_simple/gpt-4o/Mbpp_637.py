def noprofit_noloss(cost_price, selling_price):
    return cost_price == selling_price

# Tests
assert noprofit_noloss(1500, 1200) == False
assert noprofit_noloss(100, 100) == True
assert noprofit_noloss(2000, 5000) == False
