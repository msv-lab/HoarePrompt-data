import sys

# Read the input values
n, p, k = map(int, input().split())
timestamps = list(map(int, input().split()))

# Initialize the total time to zero
total_time = 0

# Calculate the time for each segment
for i in range(n):
    # If it's the first segment, calculate the time from start to the first timestamp
    if i == 0:
        total_time += timestamps[i]
    # For other segments, calculate the time between two consecutive timestamps
    else:
        total_time += (timestamps[i] - timestamps[i-1])
    
    # Calculate the speed for the current segment
    speed = 1 + (i * p/100)
    
    # Calculate the actual time for the current segment
    actual_time = total_time / speed
    
    # Add the actual time to the total time
    total_time += actual_time

# Add the remaining time after the last timestamp
total_time += (k - timestamps[-1])

# Print the total time rounded to 6 decimal places
print('{:.6f}'.format(total_time))