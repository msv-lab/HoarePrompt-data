import math

# Read input
k1, k2, k3 = map(int, input().split())

# Calculate the GCD of the three intervals
gcd_k1_k2 = math.gcd(k1, k2)
gcd_all = math.gcd(gcd_k1_k2, k3)

# If the GCD is 1, it is possible to cover every second
if gcd_all == 1:
    print("YES")
else:
    print("NO")
