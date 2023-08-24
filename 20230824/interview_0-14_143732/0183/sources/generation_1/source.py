def count_numbers(n, k, m):
    # Initialize count and result variables
    count = 0
    result = 0
    
    # Iterate over all possible x values
    for x in range(10**(n-1), 10**n):
        # Check if y exists such that y % k = 0
        if x % k == 0:
            # Increment count and add x to result
            count += 1
            result += x
    
    # Return the result modulo m
    return result % m

# Read inputs
n, k, m = map(int, input().split())

# Calculate and print the count modulo m
print(count_numbers(n, k, m))