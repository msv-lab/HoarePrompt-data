def check_tuplex(tup, element):
    return element in tup

# Test cases
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r') == True
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5') == False
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3) == True
