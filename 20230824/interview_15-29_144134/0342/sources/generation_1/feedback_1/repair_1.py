a, b, c = map(int, input().split())

# Check if a, b, and c are positive integers
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. The number of strings must be positive integers.")
else:
    # Calculate the maximum possible length of a good string
    max_length = 2 * min(a, b) + 2 * c

    # If there are remaining "a" or "b" strings, add 1 to the maximum length
    if a > 0 and b > 0:
        max_length += 1

    print(max_length)