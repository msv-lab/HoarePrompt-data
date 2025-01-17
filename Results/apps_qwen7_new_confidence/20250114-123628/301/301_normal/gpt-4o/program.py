import math

# Reading input
n = int(input())
grades = list(map(int, input().split()))

# Calculate the current sum and average
current_sum = sum(grades)

# Calculate the required sum to achieve an average of 4.5 or higher
required_sum = math.ceil(4.5 * n)

# If current sum is already sufficient
if current_sum >= required_sum:
    print(0)
else:
    # Calculate the deficit
    deficit = required_sum - current_sum
    
    # Sort grades in ascending order (prefer to replace lower grades first)
    grades.sort()
    
    # Initialize the count of lab works to redo
    redo_count = 0
    
    # Iterate through the grades and replace them with 5 until the deficit is covered
    for grade in grades:
        if deficit <= 0:
            break
        if grade < 5:
            deficit -= (5 - grade)
            redo_count += 1
    
    print(redo_count)
