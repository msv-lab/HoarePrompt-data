# Read input values
n, k, d = map(int, input().split())
a = list(map(int, input().split()))

# Sort the list of pencil saturations
a.sort()

# DP array to check the possibility of forming valid boxes
dp = [0] * (n + 1)
dp[0] = 1  # Base case: no pencils means it's trivially possible

# Sum array to maintain cumulative sums of dp values for efficient range sum calculation
sum_dp = [0] * (n + 1)
sum_dp[0] = dp[0]

# Iterate through the pencils to fill the dp table
for i in range(1, n + 1):
    left = i - k  # Minimum number of pencils required in the current box
    right = i - 1  # Current position

    # Calculate the range for valid pencils
    if left >= 0 and a[right] - a[left] <= d:
        if left == 0:
            dp[i] = 1
        else:
            dp[i] = (sum_dp[right] - sum_dp[left - 1]) > 0
    
    # Update the cumulative sum array
    sum_dp[i] = sum_dp[i - 1] + dp[i]

# Check the final state of dp array to determine the result
if dp[n] == 1:
    print("YES")
else:
    print("NO")
