n = int(input())

# Find the remainder when n is divided by 10
remainder = n % 10

# If the remainder is less than or equal to 5, round down
# Otherwise, round up
if remainder <= 5:
    result = n - remainder
else:
    result = n + (10 - remainder)

print(result)
