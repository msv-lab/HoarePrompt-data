def check_monthnumb_number(month):
    # List of months with 31 days
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    return month in months_with_31_days

# Test cases
assert check_monthnumb_number(5) == True
assert check_monthnumb_number(2) == False
assert check_monthnumb_number(6) == False
assert check_monthnumb_number(1) == True
assert check_monthnumb_number(12) == True
assert check_monthnumb_number(11) == False
