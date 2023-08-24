P, Q, R = map(int, input().split())

# Calculate the sum of flight times for each possible route
route1 = P + Q
route2 = P + R
route3 = Q + R

# Find the minimum sum of flight times among all routes
min_sum = min(route1, route2, route3)

# Print the minimum sum of flight times
print(min_sum)