t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    cards_per_player = n // k

    if m <= cards_per_player:
        print(m)
    else:
        remaining_jokers = m - cards_per_player
        remaining_players = k - 1
        max_points = cards_per_player - (remaining_jokers + remaining_players - 1) // remaining_players
        print(max_points)