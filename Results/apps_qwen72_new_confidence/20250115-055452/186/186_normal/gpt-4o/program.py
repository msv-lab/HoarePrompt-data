n, k = map(int, input().split())

# Calculate the minimum number of moves required
# The general formula derived from the explanation is:
# (number_of_moves_to_throw_stones * (n-1)) + (number_of_moves_to_pick_coins)
# where n-1 is the number of manholes to be processed (excluding the starting manhole)

total_moves = 3 * n - 3 + min(k - 1, n - k)
print(total_moves)
