n, m = map(int, input().split())

# calculate the maximum possible height for two-block pieces
max_height_two_blocks = n * 2

# calculate the maximum possible height for three-block pieces
max_height_three_blocks = m * 3

# find the maximum height among the two-block and three-block towers
max_height = max(max_height_two_blocks, max_height_three_blocks)

# check if there are enough students using two-block or three-block pieces
# to make the maximum height unique
if n >= max_height // 2 and m >= max_height // 3:
    print(max_height)
else:
    # if not enough students, increment the maximum height until it is unique
    while n < max_height // 2 or m < max_height // 3:
        max_height += 1
    print(max_height)