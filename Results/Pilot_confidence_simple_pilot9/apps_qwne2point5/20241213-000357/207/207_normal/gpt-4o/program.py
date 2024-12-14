def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def sum_frog_reachable_positions(m, a, b):
    g = gcd(a, b)
    if g != 1:
        # If gcd(a, b) != 1, we can reduce the problem by the gcd factor
        return sum_frog_reachable_positions(m // g, a // g, b // g) * g
    
    # We now have gcd(a, b) == 1
    # The sum of reachable positions for all i from 0 to m
    # f(i) = i + 1 for i >= a + b - gcd(a, b) - 1
    k = a + b - 1
    
    if m < k:
        return (m + 1) * (m + 2) // 2
    
    sum_k = k * (k + 1) // 2
    sum_m = (m * (m + 1) // 2) - ((k * (k - 1)) // 2)
    
    return sum_k + sum_m

# Reading input
m, a, b = map(int, input().split())

# Calculating the result
result = sum_frog_reachable_positions(m, a, b)

# Printing the result
print(result)
