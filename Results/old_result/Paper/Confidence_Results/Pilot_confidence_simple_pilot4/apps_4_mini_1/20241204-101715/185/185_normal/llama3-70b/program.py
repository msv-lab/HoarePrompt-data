l, r, a = map(int, input().split())
team_size = min(l, r) * 2
extra_players = (a // 2) * 2
print(team_size + extra_players)
