n, m = map(int, input().split())

# calculate the maximum possible height for two-block pieces
max_height_two_blocks = n * 2

# calculate the maximum possible height for three-block pieces
max_height_three_blocks = m * 3

# find the maximum height among the two-block and three-block towers
max_height = max(max_height_two_blocks, max_height_three_blocks)

# iterate through all possible heights starting from the maximum height
for height in range(max(max_height_two_blocks, max_height_three_blocks), max_height + 1):
    # check if there are enough students using two-block or three-block pieces
    # to make the height unique
    if n >= height // 2 and m >= height // 3:
        print(height)
        break