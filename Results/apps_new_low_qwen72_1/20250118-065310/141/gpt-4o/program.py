def min_coins_to_cover_street(n, m, antennas):
    # Initialize a list to store the minimum coins required to cover each position upto m
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # no coins needed to cover position 0

    # Sort antennas by their positions
    antennas.sort()

    # Process each antenna
    for x, s in antennas:
        # Calculate the range the current antenna covers initially
        left = max(0, x - s)
        right = min(m, x + s)

        # Update the dp table for positions covered by the initial range of the current antenna
        for j in range(left, right + 1):
            dp[j] = min(dp[j], dp[max(0, left - 1)])

        # Expand the range of the current antenna by incrementing its scope
        for j in range(right + 1, m + 1):
            dp[j] = min(dp[j], dp[max(0, j - (2 * x))] + (j - right))

    # If the last position is still inf, it means it's not covered
    return dp[m] if dp[m] != float('inf') else -1

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

antennas = []
for i in range(n):
    x = int(data[2 + 2 * i])
    s = int(data[2 + 2 * i + 1])
    antennas.append((x, s))

# Compute and print the result
print(min_coins_to_cover_street(n, m, antennas))
