def min_tallest_tower(n, m):
    max_height = 0
    if n > 0:
        max_height = max(max_height, 2 * n)
    if m > 0:
        max_height = max(max_height, 3 * m)
    print(max_height)

# Read input
n, m = map(int, input().split())

# Get the result
min_tallest_tower(n, m)
