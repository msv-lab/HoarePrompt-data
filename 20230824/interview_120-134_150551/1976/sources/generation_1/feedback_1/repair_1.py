n, m, k, q = map(int, input().split())

broken_pixels = []
for _ in range(q):
    x, y, t = map(int, input().split())
    broken_pixels.append((x, y, t))

# Initialize the time when the monitor becomes broken
min_broken_time = float('inf')

# Iterate over all possible top-left corners of the k x k square
for i in range(n - k + 1):
    for j in range(m - k + 1):
        # Check if there is any broken pixel inside the k x k square
        is_broken = False
        for pixel in broken_pixels:
            x, y, t = pixel
            if i <= x < i + k and j <= y < j + k:
                is_broken = True
                break
        # If there is no broken pixel inside the k x k square, update the min_broken_time
        if not is_broken:
            min_broken_time = min(min_broken_time, max(t for _, _, t in broken_pixels))

# If the min_broken_time is still infinity, it means the monitor is not broken
if min_broken_time == float('inf'):
    print(-1)
else:
    print(min_broken_time)