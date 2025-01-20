def longest_polyline(n, m):
    if n >= 2 and m >= 2:
        # If both n and m are greater than or equal to 2, we can use this configuration
        points = [(0, 0), (n, 0), (n, m), (0, m)]
    elif n == 0:
        # If n is 0, we are limited to vertical movement
        points = [(0, 0), (0, m), (0, 1), (0, m-1)]
    elif m == 0:
        # If m is 0, we are limited to horizontal movement
        points = [(0, 0), (n, 0), (1, 0), (n-1, 0)]
    elif n == 1:
        # If n is 1, we have limited horizontal movement
        points = [(0, 0), (1, 0), (1, m), (0, m)]
    else:  # m == 1
        # If m is 1, we have limited vertical movement
        points = [(0, 0), (0, 1), (n, 1), (n, 0)]
    return points

# Read input
n, m = map(int, input().split())

# Get the longest polyline points
result = longest_polyline(n, m)

# Print the points
for point in result:
    print(point[0], point[1])
