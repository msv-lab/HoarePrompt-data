n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

MOD = 10**9 + 7

# Find the cumulative sum of the differences between x coordinates
# to calculate the width of each rectangle
x_diff = [x[i+1] - x[i] for i in range(n-1)]

# Find the cumulative sum of the differences between y coordinates
# to calculate the height of each rectangle
y_diff = [y[i+1] - y[i] for i in range(m-1)]

# Calculate the total area by summing the products of width and height
total_area = sum(x_diff) * sum(y_diff)

# Print the total area modulo 10^9+7
print(total_area % MOD)