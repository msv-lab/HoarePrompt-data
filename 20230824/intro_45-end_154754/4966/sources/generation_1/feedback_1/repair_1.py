import sys

# Read the input values
n, p, k = map(int, sys.stdin.readline().split())
timestamps = list(map(int, sys.stdin.readline().split()))

# Initialize the total time to zero
total_time = 0

# Calculate the time for each segment
for i in range(n):
    # Calculate the speed for the current segment
    speed = 1 + (i * p/100)
    
    # Calculate the actual time for the current segment
    actual_time = (timestamps[i] - timestamps[i-1]) / speed if i != 0 else timestamps[i] / speed
    
    # Add the actual time to the total time
    total_time += actual_time

# Calculate the speed for the last segment
speed = 1 + ((n-1) * p/100)

# Add the remaining time after the last timestamp
total_time += (k - timestamps[-1]) / speed

# Print the total time rounded to 6 decimal places
print('{:.6f}'.format(total_time))