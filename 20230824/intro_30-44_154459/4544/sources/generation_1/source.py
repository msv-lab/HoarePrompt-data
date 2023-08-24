N = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the sequence
min_val = min(a)
max_val = max(a)

# Initialize a dictionary to store the count of each value
count = {}

# Iterate through the sequence
for num in a:
    # If the value is already in the dictionary, increment its count
    if num in count:
        count[num] += 1
    # If the value is not in the dictionary, add it with count 1
    else:
        count[num] = 1

# Iterate through the dictionary to find the maximum count
max_count = 0
for val in count.values():
    max_count = max(max_count, val)

# Print the maximum count
print(max_count)