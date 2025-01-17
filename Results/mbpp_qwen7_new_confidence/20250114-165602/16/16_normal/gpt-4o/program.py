def check(n):
    # Convert the number to a string to reverse its digits
    reversed_n = int(str(n)[::-1])
    # Check if the number is one less than twice its reverse
    return n == 2 * reversed_n - 1

# Provided tests
assert check(70) == False
assert check(23) == False
assert check(73) == True
