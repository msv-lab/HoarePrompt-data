import bisect

N = int(input())
values = list(map(int, input().split()))

# Sort the values in ascending order
values.sort()

# Keep merging the ingredients until only one is left
while len(values) > 1:
    # Take the two smallest values and calculate the new value
    new_value = (values[0] + values[1]) / 2
    # Remove the two smallest values
    values = values[2:]
    # Insert the new value at the correct index
    insertion_index = bisect.bisect_left(values, new_value)
    values.insert(insertion_index, new_value)

# Print the maximum possible value of the last ingredient remaining
print(values[-1])