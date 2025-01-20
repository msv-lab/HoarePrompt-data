n = int(input())
ratings = list(map(int, input().split()))
ratings.sort()
team1 = ratings[:n]
team2 = ratings[n:]
possible = all((team1[i] < team2[i] for i in range(n)))
if possible:
    print('YES')
else:
    print('NO')