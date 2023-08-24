a1, b1, a2, b2, L, R = map(int, input().split())

# Find the smallest possible value for k' and l'
k_prime = max(0, (L - b1) // a1)
l_prime = max(0, (L - b2) // a2)

# Find the largest possible value for k' and l'
k_double_prime = (R - b1) // a1
l_double_prime = (R - b2) // a2

# Calculate the number of integers x
num_x = max(0, min(k_double_prime, l_double_prime) - max(k_prime, l_prime) + 1)

print(num_x)