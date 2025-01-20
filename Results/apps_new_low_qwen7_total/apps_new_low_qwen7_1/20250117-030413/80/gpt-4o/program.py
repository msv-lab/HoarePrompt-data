MOD = 10**9 + 7

def mod_inv(a, p):
    return pow(a, p - 2, p)

def expected_length(m):
    if m == 1:
        return 1
    
    # Calculate the sum of lengths
    length_sum = 0
    for i in range(1, m + 1):
        length_sum += mod_inv(i, MOD)
        length_sum %= MOD
    
    # The expected length is m * length_sum % MOD
    result = (m * length_sum) % MOD
    
    return result

# Read input
m = int(input().strip())

# Print the result
print(expected_length(m))
