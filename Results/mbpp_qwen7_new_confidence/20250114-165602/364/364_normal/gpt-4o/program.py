def check_smaller(tuple1, tuple2):
    for a, b in zip(tuple1, tuple2):
        if b >= a:
            return False
    return True

# Test cases
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((4, 5, 6), (3, 4, 5)) == True
assert check_smaller((11, 12, 13), (10, 11, 12)) == True
