# Read input
import sys
input = sys.stdin.read
N, M, K, L = map(int, input().split())

# Determine the minimum number of coins each friend should gift
# Total coins needed: L
# Each friend gifts x coins: M * x

# We need M * x >= L, therefore x >= L / M
# We also need M * x <= N - K to ensure all gifted coins are unique

# Calculate the minimum x
min_x = (L + M - 1) // M  # This ensures we round up the division

# Check if min_x satisfies the conditions
if M * min_x <= N - K:
    print(min_x)
else:
    print(-1)
