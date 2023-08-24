def get_sum(l, r):
    # Initialize sum to 0
    sum = 0
    
    # Loop through each number from l to r
    for i in range(l, r+1):
        # If the number is odd
        if i % 2 == 1:
            # Add it to the sum
            sum += i
        
        # If the number is even
        else:
            # Add it to the sum after dividing by 2
            sum += i // 2
    
    # Return the sum modulo 1000000007
    return sum % 1000000007


# Read input values
l, r = map(int, input().split())

# Calculate and print the sum
print(get_sum(l, r))