# Read the input values for n and k
n, k = map(int, input().split())

# Read the list of bucket sizes
a = list(map(int, input().split()))

# Initialize minimum hours to a large number
min_hours = float('inf')

# Iterate through each bucket size
for bucket_size in a:
    # Check if the bucket size divides the garden length evenly
    if k % bucket_size == 0:
        # Calculate the number of hours needed with this bucket size
        hours = k // bucket_size
        # Update the minimum hours if this is less than the current minimum
        min_hours = min(min_hours, hours)

# Print the minimum number of hours
print(min_hours)
