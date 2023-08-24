N = int(input()) # number of players
accused = {} # dictionary to store the number of times each player accuses someone else

for i in range(1, N+1):
    accused_player = int(input())
    
    if accused_player in accused:
        accused[accused_player] += 1
    else:
        accused[accused_player] = 1

mobster_count = 0

for player in range(1, N+1):
    if player in accused:
        accusation_count = accused[player]
    else:
        accusation_count = 0
    
    if accusation_count == N-1:
        mobster_count += 1

if mobster_count == 0:
    mobster_count = 1

print(mobster_count)