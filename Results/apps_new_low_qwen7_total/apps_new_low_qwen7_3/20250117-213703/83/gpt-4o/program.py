import math

# Read the input values
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Calculate the current sum of marks and the number of marks
current_sum = sum(marks)
current_count = n

# Iterate to find the minimum number of additional marks needed
while True:
    # Calculate the average with the current sum and count
    current_average = current_sum / current_count
    
    # If the average rounded up is at least 'k', we have our answer
    if math.ceil(current_average) >= k:
        print(current_count - n)
        break
    
    # Otherwise, add a maximum mark (k) and continue
    current_sum += k
    current_count += 1
