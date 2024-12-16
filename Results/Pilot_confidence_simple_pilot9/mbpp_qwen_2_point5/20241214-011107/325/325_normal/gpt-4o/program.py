def check_monthnumber_number(month: int) -> bool:
    # Define the set of months that have 30 days
    months_with_30_days = {4, 6, 9, 11}
    # Check if the given month is in the set
    return month in months_with_30_days

# Test cases to validate the solution
assert check_monthnumber_number(6) == True
assert check_monthnumber_number(2) == False
assert check_monthnumber_number(12) == False
