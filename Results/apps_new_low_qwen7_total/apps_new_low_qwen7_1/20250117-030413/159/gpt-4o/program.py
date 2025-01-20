# Read input
n = int(input())
ratings = list(map(int, input().split()))

# Sort the ratings
ratings.sort()

# Split the sorted ratings into two teams
team1 = ratings[:n]
team2 = ratings[n:]

# Check if every player in team1 has a higher rating than every player in team2
possible = all(team1[i] < team2[i] for i in range(n))

# Output the result
if possible:
    print("YES")
else:
    print("NO")
