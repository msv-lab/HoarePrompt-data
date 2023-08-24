N = int(input()) # number of players
accused = {} # dictionary to store the number of times each player is accused

for i in range(1, N+1):
    accused_player = int(input())
    if accused_player in accused:
        accused[accused_player] += 1
    else:
        accused[accused_player] = 1

mobster_count = 0

for player, accusation_count in accused.items():
    if accusation_count > mobster_count:
        mobster_count = accusation_count

print(mobster_count)