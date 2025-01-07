# Read input values
n = int(input())
a = int(input())
b = int(input())

# Calculate the total length needed for two door frames
total_length_needed = 2 * (2 * a + b)

# Calculate the minimal number of wooden bars required
minimal_bars_needed = (total_length_needed + n - 1) // n

# Print the result
print(minimal_bars_needed)
