def convert_to_decimal(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
    return decimal_value

# Read input
n, base_x = map(int, input().split())
digits_x = list(map(int, input().split()))
m, base_y = map(int, input().split())
digits_y = list(map(int, input().split()))

# Convert both numbers to decimal
decimal_x = convert_to_decimal(digits_x, base_x)
decimal_y = convert_to_decimal(digits_y, base_y)

# Compare and print result
if decimal_x < decimal_y:
    print('<')
elif decimal_x > decimal_y:
    print('>')
else:
    print('=')
