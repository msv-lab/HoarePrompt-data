def dog_age(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

# Testing the function with given test cases
assert dog_age(12) == 61
assert dog_age(15) == 73
assert dog_age(24) == 109
