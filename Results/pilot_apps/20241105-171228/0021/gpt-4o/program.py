n = int(input())
a = list(map(int, input().split()))

# Find the initial positions of the minimum and maximum elements
min_pos = a.index(1)
max_pos = a.index(n)

# Calculate possible new distances after performing one swap
# Option 1: Swap the minimum element with the element at the start
dist1 = abs(0 - max_pos)
# Option 2: Swap the minimum element with the element at the end
dist2 = abs((n-1) - max_pos)
# Option 3: Swap the maximum element with the element at the start
dist3 = abs(0 - min_pos)
# Option 4: Swap the maximum element with the element at the end
dist4 = abs((n-1) - min_pos)

# The maximum possible distance after one swap
max_distance = max(dist1, dist2, dist3, dist4)
print(max_distance)
