n, m = map(int, input().split())
sky_map = [input().strip() for _ in range(n)]

min_row, max_row = n, -1
min_col, max_col = m, -1

# Find the bounding box of the stars
for i in range(n):
    for j in range(m):
        if sky_map[i][j] == '*':
            if i < min_row:
                min_row = i
            if i > max_row:
                max_row = i
            if j < min_col:
                min_col = j
            if j > max_col:
                max_col = j

# Calculate the side length of the square that can cover all stars
side_length = max(max_row - min_row + 1, max_col - min_col + 1)

print(side_length)
