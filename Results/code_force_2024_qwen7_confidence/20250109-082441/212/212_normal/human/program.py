M = 10**9 + 7

for tc in range(int(input())):
    # Read the number of children, friend pairs, and excursions
    n, m, k = map(int, input().split())
    
    # Initialize the sum of initial friendship values
    s = 0
    
    # Read each friend pair and accumulate their initial friendship values
    for i in range(m):
        x, y, f = map(int, input().split())
        s += f
    
    # Calculate the total number of possible pairs
    total_pairs = n * (n - 1) // 2
    
    # Calculate the modular inverse of total_pairs
    d = pow(total_pairs, M - 2, M)
    
    # Calculate the probability of choosing a friend pair
    p = m * d
    
    # Calculate the expected value of the sum of friendship values
    c = (k * s) + p * (k * (k - 1) // 2)
    
    # Calculate the final result using modular arithmetic
    result = (c * d) % M
    
    # Output the result for the current test case
    print(result)