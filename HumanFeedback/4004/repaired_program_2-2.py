# Read the input values
n = int(input())
a = list(map(int, input().split()))

# Find the distinct values in the array
distinct_values = set(a)

# Check the number of distinct values
distinct_count = len(distinct_values)

# Handle each scenario separately
if distinct_count == 1:
    # All values are already equal, so no changes needed
    print(0)
elif distinct_count == 2:
    # Get the minimum and maximum values
    min_val = min(a)
    max_val = max(a)

    # Calculate the difference between the two values
    diff = max_val - min_val

    # Check if the difference is divisible by 2
    if diff % 2 == 0:
        # There is a valid value of D to make all values equal
        print(diff // 2)
    else:
        # It is not possible to make all values equal
        print(-1)
else:
    # More than 2 distinct values, check the differences between sorted values
    sorted_values = sorted(distinct_values)

    # Check if the differences are the same
    if sorted_values[1] - sorted_values[0] != sorted_values[2] - sorted_values[1]:
        # The differences are not the same, cannot make all values equal
        print(-1)
    else:
        # Calculate the difference between the target value and each element
        diff = sorted_values[1] - sorted_values[0]

        # Check if the difference is divisible by 2
        if diff % 2 == 0:
            # There is a valid value of D to make all values equal
            print(diff // 2)
        else:
            # It is not possible to make all values equal
            print(-1)