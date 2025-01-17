from bisect import bisect_left

# Function to read input values
def read_input():
    return map(int, input().split())

# Function to calculate the modular inverse using Fermat's Little Theorem
def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

# Read the number of test cases
t, = read_input()

# Iterate over each test case
for _ in range(t):
    # Read the number of balls and baskets
    n, m = read_input()
    
    # Read the initial positions of the balls
    a = list(read_input())
    
    # Sort the positions of the balls
    a.sort()
    
    # Calculate the distances between consecutive balls
    distances = [a[i + 1] - a[i] for i in range(n - 1)]
    
    # Append the distance from the last ball to the first ball in the circle
    distances.append(m - a[-1] + a[0])
    
    # Sort the distances
    distances.sort()
    
    # Initialize the expected time
    expected_time = 0
    
    # Calculate the expected time using the given formula
    for i in range(n):
        expected_time += (distances[i] * (i + 1) * (n - i)) % 1000000007
    
    # Multiply by 2 and adjust for modular arithmetic
    expected_time = (expected_time * 2) % 1000000007
    
    # Calculate the modular inverse of the total number of combinations
    inverse_combinations = mod_inverse(n * (n + 1) // 2, 1000000007)
    
    # Final result is the expected time multiplied by the inverse of combinations
    result = (expected_time * inverse_combinations) % 1000000007
    
    # Output the result for the current test case
    print(result)