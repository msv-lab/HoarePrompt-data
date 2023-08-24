def count_numbers(n, k, m):
    # Initialize count and result variables
    count = 0
    result = 0
    
    # Iterate over all possible x values
    for x in range(10**(n-1) + 1, 10**n):
        # Check if y exists such that y % k = 0
        for suffix_length in range(1, n+1):
            y = x % (10**suffix_length)
            if y % k == 0:
                # Increment count and add x to result
                count += 1
                result += x
                break
    
    # Return the count modulo m
    return count % m

# Read inputs
n, k, m = map(int, input().split())

# Calculate and print the count modulo m
print(count_numbers(n, k, m))