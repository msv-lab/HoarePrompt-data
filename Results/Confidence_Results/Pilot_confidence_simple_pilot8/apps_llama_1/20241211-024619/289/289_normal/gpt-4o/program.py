n = int(input())

# The maximum number of games the winner can play is essentially the maximum number of times
# we can divide the number of players by 2 (which is equivalent to finding the highest power
# of 2 less than or equal to n).
max_games = n.bit_length() - 1

print(max_games)
