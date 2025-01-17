def calculate_games(num_teams):
    games = 0
    while num_teams % 2 == 0:
        games += num_teams // 2
        num_teams //= 2
    if num_teams > 1:
        games += num_teams * (num_teams - 1) // 2
    return games

def find_teams_for_games(n):
    results = []
    for teams in range(1, n + 1):
        if calculate_games(teams) == n:
            results.append(teams)
        if teams * (teams - 1) // 2 > n:
            break
    return results

n = int(input())
results = find_teams_for_games(n)
if results:
    for team in results:
        print(team)
else:
    print(-1)
