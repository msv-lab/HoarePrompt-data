import sys
import math

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Initialize index for reading data
index = 0

# Number of test cases
t = int(data[index])
index += 1

# Process each test case
results = []
for _ in range(t):
    # Read grid dimensions
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    # Initialize the result for the current test case
    max_gcd = 0
    
    # Iterate over each row
    for _ in range(n):
        # Read the row elements
        row = list(map(int, data[index:index + m]))
        index += m
        
        # Calculate the GCD of the current row
        row_gcd = 0
        for num in row:
            row_gcd = math.gcd(row_gcd, num)
        
        # Update the maximum GCD for the grid
        max_gcd = math.gcd(max_gcd, row_gcd)
    
    # Store the result for the current test case
    results.append(max_gcd)

# Output results for all test cases
for result in results:
    print(result)