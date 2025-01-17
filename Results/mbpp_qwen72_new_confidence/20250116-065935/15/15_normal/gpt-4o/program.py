def is_woodall(num):
    n = 1
    while True:
        woodall_num = n * (2 ** n) - 1
        if woodall_num == num:
            return True
        elif woodall_num > num:
            return False
        n += 1

# Test cases
assert is_woodall(383) == True
assert is_woodall(254) == False
assert is_woodall(200) == False
