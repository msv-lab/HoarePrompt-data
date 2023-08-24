n = int(input())

# Calculate the expected total number of gifts taken out for a family of size n
def calculate_expected_total_gifts(n):
    if n == 2:
        return 3.0
    
    # Initialize variables
    E = [0.0] * (n + 1)
    E[2] = 3.0
    
    # Calculate E(n) iteratively for n = 3 to n
    for i in range(3, n):
        E[i] = 1 / (i - 1) * E[i - 1] + 1.0
    
    return E[n]

# Print the result with 9 decimal places precision
print(format(calculate_expected_total_gifts(n), '.9f'))