# Read the input
a, b = map(int, input().split())

# Process the values of a and b based on the given rules
while a != 0 and b != 0:
    if a >= 2 * b:
        a %= 2 * b
    elif b >= 2 * a:
        b %= 2 * a
    else:
        break

# Output the final values of a and b
print(a, b)
